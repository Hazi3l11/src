from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI

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