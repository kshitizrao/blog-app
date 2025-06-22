from pydantic import BaseModel
from typing import List



class Blog(BaseModel) : # This is a Pydantic model for the blog schemas
    title: str
    body: str


class User(BaseModel):
    username: str
    email: str
    password: str

class showUser(BaseModel):
    username: str
    email: str
    blogs : List[Blog] = []
    class config:
        orm_mode = True    

class showBlog(BaseModel): # This is a Pydantic model for displaying a blog entry where it is only showing the title
    title: str
    body: str
    creator: showUser  # Assuming Creator is a string representing the username of the blog creator
    class Config:
        orm_mode = True
        # This allows the model to work with ORM objects, enabling serialization and deserialization of ORM models
        # It tells Pydantic to treat the ORM model as a dictionary-like object, allowing it to read attributes directly from the ORM model
