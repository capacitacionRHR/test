from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hola" : "Mundo"}

# @app.get("/item/{item_id}")
# def read_item(item_id: int, query_param: str = None ):
#     return {"item_id": item_id, "query_params": query_param}


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = False

# @app.put("/item/{item_id}")
# def update_item(item_id : int, item: Item):
#     return {"item_id": item_id, "item_name": item.name}

# @app.get("/item/{item_id}")
# def read_item(item_id : int):
#     if item_id == 0:
#         raise HTTPException(status_code=404, detail="El item no se encuentra")
#     return {"item_id": item_id}


app = FastAPI(title="API de gestion de tareas")


# Modelo de datos
class Tarea(BaseModel):
    titulo : str
    descripcion: str
    completada: bool = False

tareas : List[Tarea] = []

#Crear una tarea
@app.post("/tareas", response_model = Tarea)
def crear_tarea(tarea: Tarea):
    tareas.append(tarea)
    return tarea

# Listar tareas
@app.get("/tareas", response_model = List[Tarea])
def listar_tareas():
    return tareas

# Ver una tarea en especifico
@app.get("/tareas/{id}", response_model = Tarea)
def obtener_tarea(id: int):
    if id < 0 or id >= len(tareas):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tareas[id]

# Actualizar tarea a completada
@app.put("/tareas/{id}/completar", response_model = Tarea)
def completar_tarea(id:int):
    if id < 0 or id >= len(tareas):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tareas[id].completada = True
    return tareas[id]

# Eliminar tarea
@app.delete("/tareas/{id}")
def eliminar_tarea(id:int):
    if id < 0 or id >= len(tareas):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_eliminada = tareas.pop(id)
    return {"mensaje": "Tarea eliminada", "tarea eliminada": tarea_eliminada}
