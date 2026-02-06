from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

#Modelos
class Cliente(BaseModel):
    id_cliente:int
    nombre:str
    email:str
    telefono:str

class Vehiculo(BaseModel):
    id:int
    marca: str
    modelo: str
    año: int
    cliente_id: int

class Servicio(BaseModel):
    id:int
    descripcion: str
    costo: float
    vehiculo_id:int

clientes: List [Cliente] = []
vehiculos: list [Vehiculo] = []
servicios: list [Servicio] = []
#Clientes
@app.post("/clientes/")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {"msg": "Cliente agregado", "cliente": cliente}

@app.get("/clientes/")
def mostrar_clientes():
    return clientes

#Vehiculos
@app.post("/vehiculos/")
def crear_vehiculo(vehiculo: Vehiculo):
    vehiculos.append(vehiculo)
    return {"msg": "Vehiculo agregado", "vehiculo": vehiculo}

@app.get("/vehiculos/")
def mostrar_vehiculos():
    return vehiculos
#Servicios
@app.post("/servicios/")
def crear_servicio(servicio: Servicio):
    servicios.append(servicio)
    return {"msg": "Servicio agregado", "servicio": servicio}

@app.get("/servicios/")
def mostrar_servicios():
    return servicios
