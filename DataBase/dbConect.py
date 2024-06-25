import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# conn = psycopg2.connect(database="cadernos",
#                         host="localhost",
#                         user="admin",
#                         password="#3!ba42",
#                         port="5432")


DATABASE_URL = "postgresql://admin:#3!ba42@localhost:5432/cadernosv7"
engine= create_engine(DATABASE_URL)
SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
