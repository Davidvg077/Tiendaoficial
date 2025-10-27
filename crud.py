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
    
async def obtener_categorias():
    with Session(engine) as session:
        categorias = session.exec(select(Categoria).where(Categoria.activa == True)).all()
        return categorias    