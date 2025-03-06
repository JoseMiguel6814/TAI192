from pydantic import BaseModel, Field, EmailStr


#modelo de  validacion
class ModeloUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre: str = Field(..., min_length=3, max_length=50, description="solo letras y minimo 3 caracteres y maximo 50")
    edad: int = Field(..., gt=0,lt=121 ,description="solo numeros positivos")
  
    correo:EmailStr = Field(..., description="correo electronico", examples=["correo@gmail.com"])


class modeloAuth(BaseModel):
   email:EmailStr = Field(..., description="correo electronico")
   passw: str = Field(...,min_length=8, strip_whitespace=True, description="contraseña")

   