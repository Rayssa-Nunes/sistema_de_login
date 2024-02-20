from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    USER = os.getenv('USUARIO')
    PASSWORD = os.getenv('SENHA')
    DB = os.getenv('BANCO_DE_DADOS')

    return create_engine(f'postgresql://{USER}:{PASSWORD}@localhost:5432/{DB}', echo=True)
    
engine = get_engine()
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(150))

Base.metadata.create_all(engine)
