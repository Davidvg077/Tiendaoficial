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
    
async def obtener_categoria(id: int):
    with Session(engine) as session:
        categoria = session.get(Categoria, id)
        return categoria    
    
async def eliminar_categoria(id: int):
    with Session(engine) as session:
        categoria = session.get(Categoria, id)
        if categoria:
            session.delete(categoria)
            session.commit()
            return True
        return False    

async def obtener_categoria_con_productos(id: int):
    from sqlalchemy.orm import selectinload
    with Session(engine) as session:
        categoria = session.exec(select(Categoria).where(Categoria.id == id).options(selectinload(Categoria.productos))).first()
        if categoria:
            # Devolver como dict para evitar lazy loading issues
            return {
                "id": categoria.id,
                "nombre": categoria.nombre,
                "descripcion": categoria.descripcion,
                "activa": categoria.activa,
                "productos": [
                    {
                        "id": p.id,
                        "nombre": p.nombre,
                        "descripcion": p.descripcion,
                        "precio": p.precio,
                        "stock": p.stock,
                        "activo": p.activo,
                        "categoria_id": p.categoria_id,
                        "categoria": {
                            "id": categoria.id,
                            "nombre": categoria.nombre,
                            "descripcion": categoria.descripcion,
                            "activa": categoria.activa
                        }
                    } for p in categoria.productos
                ]
            }
        return None        
    
    
async def actualizar_categoria(id: int, categoria_update):
    with Session(engine) as session:
        categoria = session.get(Categoria, id)
        if categoria:
            for key, value in categoria_update.dict(exclude_unset=True).items():
                setattr(categoria, key, value)
            session.commit()
            session.refresh(categoria)
            return categoria
        return None