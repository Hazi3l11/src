from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title = "Taller Mecanico")

class Cliente(BaseModel):
    id:int
    nombre:str
    email:str

class Vehiculo(BaseModel):
    id:int
    marca: str
    modelo: str

class Servicio(BaseModel):
    id:int
    descripcion:str
    costo: float

cliente: List [Cliente] = []
vehiculo: list [Vehiculo] = []
servicio: list [Servicio] = []

#Definir los Endpoints
@app.get("/clientes", response_model=List[Cliente])
def mostrar_clientes():
    return cliente

@app.get("/vehiculos", response_model=List[Vehiculo])
def mostrar_clientes():
    return vehiculo

@app.get("/servicios", response_model=List[Servicio])
def mostrar_clientes():
    return servicio