# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cadena de conexión a la base de datos PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://login_as_user:hdc5GgXhPdBHos2pTia0BfVJUnNFBNCH@dpg-cpie1da1hbls73bge5a0-a.oregon-postgres.render.com/login_as"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
