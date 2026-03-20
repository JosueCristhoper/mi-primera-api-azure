from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hola desde Azure!!!", "autor": "Josue"}

@app.get("/saludar/{nombre}")
def saludar_usuario(nombre: str):
    return {
        "mensaje": f"Hola {nombre}, bienvenido a mi API en Azure",
        "tecnologia": "FastAPI",
        "estado": "Online"
    }