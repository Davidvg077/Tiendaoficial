from fastapi import FastAPI, HTTPException
from models import Categoria, Producto
from database import init_db
import crud
from Schemas import CategoriaUpdate, ProductoUpdate, CategoriaConProductos, ProductoResponse, ProductoListResponse, RestarStock

app = FastAPI(title="API Tienda con SQLModel")

# Crear la base de datos al iniciar
@app.on_event("startup")
def startup_event():
    init_db()


# Endpoints de categorias

@app.post("/categorias/", response_model=Categoria)
async def crear_categoria(categoria: Categoria):
    return await crud.crear_categoria(categoria)

@app.get("/categorias/", response_model=list[Categoria])
async def obtener_categorias():
    return await crud.obtener_categorias()    