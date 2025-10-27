from pydantic import BaseModel, Field, conint, constr
from typing import Optional, List

# Esquemas de Categoria 

class CategoriaBase(BaseModel):
    nombre: constr(min_length=1, max_length=100)
    descripcion: Optional[str] = None
    activa: Optional[bool] = True

class CategoriaCreate(CategoriaBase):
    """Esquema para crear una categoría"""
    pass

class CategoriaUpdate(BaseModel):
    """Esquema para actualizar una categoría"""
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    activa: Optional[bool] = None

class CategoriaResponse(CategoriaBase):
    """Esquema de respuesta que incluye ID y productos"""
    id: int

    class Config:
        orm_mode = True    

# Esquemas de producto

class ProductoBase(BaseModel):
    nombre: constr(min_length=1, max_length=100)
    descripcion: Optional[str] = None
    precio: float = Field(gt=0, description="El precio debe ser mayor que 0")
    stock: conint(ge=0) = 0
    activo: Optional[bool] = True
    categoria_id: int


class ProductoCreate(ProductoBase):
    """Esquema para crear un producto"""
    pass


class ProductoUpdate(BaseModel):
    """Esquema para actualizar un producto"""
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    activo: Optional[bool] = None
    categoria_id: Optional[int] = None


class ProductoResponse(ProductoBase):
    """Esquema de respuesta de producto"""
    id: int
    categoria: Optional[CategoriaResponse] = None  # Para mostrar la categoría del producto

    class Config:
        orm_mode = True


# Relacion completa
       
class CategoriaConProductos(CategoriaResponse):
    """Devuelve la categoría con todos sus productos"""
    productos: List[ProductoResponse] = []

    class Config:
        orm_mode = True


class ProductoListResponse(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    activo: bool
    categoria_id: int
    categoria: str

    class Config:
        orm_mode = True


class RestarStock(BaseModel):
    cantidad: conint(gt=0)

