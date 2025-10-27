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
