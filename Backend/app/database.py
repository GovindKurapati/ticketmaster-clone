from sqlmodel import SQLModel, create_engine, Session
from app.config import settings

# Using SQLModel library as ORM
# Configuring the database setup
# `echo=True` enables sqlmodel logging, outputting SQL statements to the console (useful for debugging)
engine = create_engine(settings.DATABASE_URL, echo=True)


# Function to create database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Function to get a database session, providing a session object for CRUD operations
# Context manager is used to ensure the session is properly closed after use
def get_session():
    with Session(engine) as session:
        yield session
