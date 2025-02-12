from fastapi import FastAPI
from typing import Optional



app=FastAPI(
    title='API de prueba 192',
    description='Jose Miguel Perusquia Hernandez',
    version='1.0.1'
    )

usuarios = [
    {"id":1, "nombre":"Juan","edad":25},
    {"id":2, "nombre":"Maria","edad":30},
    {"id":3, "nombre":"Pedro","edad":35},
    {"id":4, "nombre":"Jose","edad":40}
]

#endpoint home
@app.get("/",tags=["hola mundo"]) 
def home():
    return {"message": "Hello World"}
    
    #endpoint de promedio
@app.get("/promedio", tags=["Mi calificacion tai api"])
def promedio():
    return {"numero": " 5.5"}
    
    #endpoint parametro obligatorio
@app.get("/usuario/{id}", tags=["Parametro obligatorio id"])
def consultaUsuario(id: int):
    #simulacion de base de datos
    #consulta = select * from usuario where id = id
    return {"se encontro el usuario con el id":id}
    
    #endpoint parametro opcional
@app.get("/usuario/", tags=["Parametro opcional nombre"])
def consultaUsuarioOpcional(id: Optional[int] = None):
    if id is not None:
        for us in usuarios:
            if us['id'] == id:
                return {"mensaje": "usuario encontrado", "usuario": us}
        return {"mensaje": f"usuario no encontrado con el id: {id}"}
    else:
        return {"mensaje": "no se proporcionó un id"}








#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}