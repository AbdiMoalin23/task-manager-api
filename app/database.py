from sqlalchemy import create_engine   #Connects Python to database
from sqlalchemy.orm import sessionmaker #Tool to talk to the Database (add,read,update)
from sqlalchemy.orm import DeclarativeBase #Base class to create ORM database models

DATABASE_URL = "sqlite:///./tasks.db" #Use Sqlite Database stored in a file called tasks.db

engine = create_engine(DATABASE_URL) #create connection to database

SessionLocal = sessionmaker(bind=engine) #create session factory

class Base (DeclarativeBase): #SqlAlchemy maps models to tables
    pass
