from fastapi import FastAPI, HTTPException,Depends
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from modelsPydantics import ModeloUsuario, modeloAuth
from genToken import createToken
from fastapi.responses import JSONResponse
from middlewares import BearerJWT
from db.conexion import Session,engine,Base
from models.modelsDB import User

Base.metadata.create_all(bind=engine)



app=FastAPI(
    title='API de prueba 192',
    description='Jose Miguel Perusquia Hernandez',
    version='1.0.1'
    )


#endpoint home
@app.get("/",tags=["hola mundo"]) 
def home():
    return {"message": "Hello World"}

#endpoint autenticacion
@app.post("/auth", tags=["Autentificacion"])
def login(autorizacion: modeloAuth):
   if autorizacion.email == "example@example.com" and autorizacion.passw == "12345678":
       token:str = createToken(autorizacion.model_dump())
       print(token)
       return JSONResponse(content={"token": token})
    

#endpoint Consultar Todos
@app.get("/todosusuarios",dependencies={Depends(BearerJWT())},response_model= List[ModeloUsuario], tags=["Operaciones Crud"])
def LeerUsuarios():
    db = Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)})


#endpoint para agregar usuario con db
@app.post("/agregarusuariodb", tags=["Operaciones Crud"])
def AgregarUsuarioDB(usuario: ModeloUsuario):
    db = Session()
    try:
        db.add(User(name=usuario.nombre, age=usuario.edad, email=usuario.correo))
        db.commit()
        return {"message": "Usuario agregado correctamente"}
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)})


#endpoint buscar usuario por id
@app.get("/buscarusuarioid/{id}", tags=["Operaciones Crud"])
def BuscarUsuarioId(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if consulta is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)})

