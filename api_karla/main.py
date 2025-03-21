from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from funciones import *

app = FastAPI()

# Serve static files (HTML, JS, CSS) from the 'static' folder
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    # This will serve the a.html file when accessing the root URL
    with open("static/a.html") as file:
        return file.read()

@app.get("/js")
def get_js():
    # Serve a specific JS file directly
    with open("static/script.js") as file:
        return file.read()
    
@app.get("/p/q/e/me/")
async def read_item(p: int, q: int, e: int, me: str):
    response = encrypt(me, e, p, q)
    # Check if the item parameter is being received correctly
    return {"received_item": response}