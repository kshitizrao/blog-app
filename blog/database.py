from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# This code sets up a SQLite database connection using SQLAlchemy for a FastAPI project.

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# Create a new SQLite database file named blog.db in the current directory
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# The connect_args={"check_same_thread": False} is necessary for SQLite to allow multiple threads to access the database


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal is a session factory that will create new Session objects when called
Base = declarative_base()
# Base is the declarative base class that maintains a catalog of classes and tables relative to that base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()