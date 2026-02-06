from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI

#Modelos
class Cliente(BaseModel):
    id:int
    nombre:str
    email:str
    telefono:str

class Vehiculo(BaseModel):
    id:int
    id_cliente:int
    marca: str
    modelo: str

class Orden_Servicio(BaseModel):
    id:int
    id_vehiculo:int
    costo: float

cliente: List [Cliente] = []
vehiculo: list [Vehiculo] = []
orden_servicio: list [Orden_Servicio] = []

#Definir los Endpoints
@app.get("/clientes", response_model=List[Cliente])
def mostrar_clientes():
    return cliente
