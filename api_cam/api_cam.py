from fastapi import FastAPI
import numpy as np
import sympy as sp

app = FastAPI()

@app.get("/suma/{a}/{b}")
def suma(a: float, b: float):
    return {"operación": "suma", "resultado": a + b}

@app.get("/resta/{a}/{b}")
def resta(a: float, b: float):
    return {"operación": "resta", "resultado": a - b}

@app.get("/multiplicacion/{a}/{b}")
def multiplicacion(a: float, b: float):
    return {"operación": "multiplicación", "resultado": a * b}

@app.get("/division/{a}/{b}")
def division(a: float, b: float):
    if b == 0:
        return {"error": "División por cero no permitida"}
    return {"operación": "división", "resultado": a / b}

@app.get("/derivada/{funcion}/{variable}")
def derivada(funcion: str, variable: str):
    x = sp.Symbol(variable)
    try:
        expr = sp.sympify(funcion)
        derivada_expr = sp.diff(expr, x)
        return {"derivada": str(derivada_expr)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/integral/{funcion}/{variable}")
def integral(funcion: str, variable: str):
    x = sp.Symbol(variable)
    try:
        expr = sp.sympify(funcion)
        integral_expr = sp.integrate(expr, x)
        return {"integral": str(integral_expr)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/matriz_aleatoria/{filas}/{columnas}")
def matriz_aleatoria(filas: int, columnas: int):
    matriz = np.random.rand(filas, columnas).tolist()
    return {"matriz_aleatoria": matriz}