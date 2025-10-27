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