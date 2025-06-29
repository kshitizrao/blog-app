from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog,user,authentication
# fastAPI_project/blog/main.py

# This code initializes a FastAPI application and creates the database tables for a blog application.
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# This line creates the database tables based on the models defined in models.py
# This code initializes a FastAPI application and creates the database tables for the blog application.


app.include_router(authentication.router) # This line includes the authentication router, which contains the endpoints for user authentication
app.include_router(blog.router) # This line includes the blog router, which contains the endpoints for managing blog entries     
app.include_router(user.router) # This line includes the user router, which contains the endpoints for managing users



