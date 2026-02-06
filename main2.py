from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

#Modelo de datos
class Platillo(BaseModel):
	nombre: str
	proteina: str
	verduras: List[str]
	salsas: List[str]

#Metodo GET
@app.get("/receta/{id_receta}")
def obetener_receta(id_receta:int):
	return {
		"mensaje" : f"Consulta la receta {id_receta}",
		"ingredientes" : ["salsa magi", "salsa inglesa"]
	}
@app.post("/cocinar")
def crear_platillo(platillo: Platillo):
	return {
		"status":"Cocinando",
		"detalle":f"preparando platillo {platillo.nombre} con {platillo.proteina}"
	}

# @app.get("/")
# def read_root():
# 	return {"Bienvenido a la materia ": "Taller 2"}
# @app.get("/producto/{producto_id}")
# def read_item(producto_id: int, q: str = None):
# 	return {"producto_id": producto_id, "SQL":q}

