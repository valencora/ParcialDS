from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la URL de la base de datos
DATABASE_URL = "sqlite:///./adn_database.db"  # Puedes cambiar esta URL según tu base de datos

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Declarar la clase base para los modelos
Base = declarative_base()

# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
