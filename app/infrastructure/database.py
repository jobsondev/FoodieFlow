import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import VARCHAR, FLOAT, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from dotenv import load_dotenv
from decouple import config

load_dotenv()

#Pegando as configuracoes do .env
DB_USER = config('POSTGRES_USER', default=os.getenv('POSTGRES_USER'))
DB_PASSWORD = config('POSTGRES_PASSWORD', default=os.getenv('POSTGRES_PASSWORD'))
DB_NAME = config('POSTGRES_DB', default=os.getenv('POSTGRES_DB'))
DB_HOST = config('POSTGRES_HOST', default=os.getenv('POSTGRES_HOST'))
#DB_PORT = config('POSTGRES_PORT', default=os.getenv('POSTGRES_PORT'))

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
#"postgresql://postgres:postgres@gestao-postgresql:5432/FIAP"
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def init_db():
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
