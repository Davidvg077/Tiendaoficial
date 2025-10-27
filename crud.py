from sqlmodel import Session, select
from models import Categoria, Producto
from database import engine

# Funciones CRUD para Categoria

async def crear_categoria(categoria: Categoria):
    with Session(engine) as session:
        session.add(categoria)
        session.commit()
        session.refresh(categoria)
        return categoria
    
    