from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import httpx
import re
import time
from collections import defaultdict
import requests
import os
from dotenv import load_dotenv

app = FastAPI()

# Configuración
load_dotenv()
#ABUSEIPDB_API_KEY = os.getenv('ABUSEIPDB_API_KEY')
ABUSEIPDB_API_KEY = "7c1e577cc11b38f152078b592ed68cfd88ad686c0362418a93cf46b6e59c2e3760589897c1646ff3"
if not ABUSEIPDB_API_KEY:
    raise ValueError("ABUSEIPDB_API_KEY environment variable not set")
RATE_LIMIT = 60  # Límite de peticiones por IP en 60 segundos

# Registro de peticiones para rate limiting
request_log = defaultdict(list)

class RequestData(BaseModel):
    data: str
    forward_url: str

# Función de validación de entrada
def validate_input(data: str):
    if len(data) > 1000:
        raise HTTPException(status_code=400, detail="Datos demasiado largos")
    if re.search(r"[<>/'\"]", data):
        raise HTTPException(status_code=400, detail="Entrada con caracteres sospechosos")

# Middleware de seguridad
@app.middleware("http")
async def security_middleware(request: Request, call_next):
    client_ip = request.client.host
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={client_ip}&maxAgeInDays=90"
    headers = {
    "Key": ABUSEIPDB_API_KEY,
    "Accept": "application/json"
    }
    print(url)
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url, headers=headers)
    except:
        response = None

    if response and response.status_code == 200:
        # Bloqueo de IPs prohibidas
        if response.json()["data"]["abuseConfidenceScore"] > 20:
            raise HTTPException(status_code=403, detail="IP bloqueada")
    
    # Protección contra bots
    user_agent = request.headers.get("User-Agent", "")
    if not user_agent or "bot" in user_agent.lower():
        raise HTTPException(status_code=403, detail="User-Agent sospechoso")
    
    # Rate limiting
    now = time.time()
    request_log[client_ip] = [t for t in request_log[client_ip] if now - t < 60]
    if len(request_log[client_ip]) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Demasiadas solicitudes, intenta más tarde")
    request_log[client_ip].append(now)
    
    return await call_next(request)

# Endpoint seguro
@app.post("/procesar")
async def procesar_request(data: RequestData, request: Request):
    validate_input(data.data)  # Validación de datos
    
    # Reenvío seguro a la URL especificada en la petición
    async with httpx.AsyncClient() as client:
        # descomentar cuando tenga otra api :c
        #response = await client.post(data.forward_url, json={"data": data.data})
        response = {"data": data.data}
    return response
    return response.json()
