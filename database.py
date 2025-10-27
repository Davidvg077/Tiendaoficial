from sqlmodel import SQLModel, create_engine

# URL de la base de datos local SQLite
DATABASE_URL = "sqlite:///tienda.db"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Función para inicializar la base de datos
def init_db():
    """
    Crea las tablas definidas en los modelos si no existen.
    """
    SQLModel.metadata.create_all(engine)