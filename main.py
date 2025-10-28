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

@app.get("/categorias/{id}", response_model=Categoria)
async def obtener_categoria(id: int):
    categoria = await crud.obtener_categoria(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@app.get("/categorias/{id}/productos")
async def obtener_categoria_con_productos(id: int):
    categoria = await crud.obtener_categoria_con_productos(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@app.put("/categorias/{id}", response_model=Categoria)
async def actualizar_categoria(id: int, categoria: CategoriaUpdate):
    categoria_actualizada = await crud.actualizar_categoria(id, categoria)
    if not categoria_actualizada:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria_actualizada

@app.patch("/categorias/{id}/desactivar", response_model=Categoria)
async def desactivar_categoria(id: int):
    categoria = await crud.desactivar_categoria(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@app.delete("/categorias/{id}")
async def eliminar_categoria(id: int):
    eliminado = await crud.eliminar_categoria(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"mensaje": "Categoría eliminada correctamente"} 

# Endpoints de productos

@app.post("/productos/", response_model=Producto)
async def crear_producto(producto: Producto):
    return await crud.crear_producto(producto)

@app.get("/productos/", response_model=list[ProductoListResponse])
async def obtener_productos():
    return await crud.obtener_productos()


@app.get("/productos/{id}", response_model=Producto)
async def obtener_producto(id: int):
    producto = await crud.obtener_producto(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.get("/productos/{id}/categoria", response_model=ProductoResponse)
async def obtener_producto_con_categoria(id: int):
    producto = await crud.obtener_producto_con_categoria(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto    

@app.put("/productos/{id}", response_model=Producto)
async def actualizar_producto(id: int, producto: ProductoUpdate):
    producto_actualizado = await crud.actualizar_producto(id, producto)
    if not producto_actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_actualizado    

@app.patch("/productos/{id}/desactivar", response_model=Producto)
async def desactivar_producto(id: int):
    producto = await crud.desactivar_producto(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto    