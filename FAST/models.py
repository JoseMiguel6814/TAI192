from pydantic import BaseModel, Field


#modelo de  validacion
class ModeloUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre: str = Field(..., min_length=3, max_length=50, description="solo letras y minimo 3 caracteres y maximo 50")
    edad: int = Field(..., gt=0,lt=121 ,description="solo numeros positivos")
  
    correo:str = Field(..., pattern=r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", examples=["example@gmail.com"])

