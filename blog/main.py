from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas,models,hashing
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
# fastAPI_project/blog/main.py

# This code initializes a FastAPI application and creates the database tables for a blog application.
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# This line creates the database tables based on the models defined in models.py
# This code initializes a FastAPI application and creates the database tables for the blog application.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
   

@app.post('/blog', status_code=status.HTTP_201_CREATED, tags = ['Blog']) # This endpoint uses the schemas.Blog model
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)  # Assuming user_id is set to 1 for simplicity
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', response_model=List[schemas.showBlog], tags = ['Blog']) # This endpoint retrieves all blog entries
def all(db: Session = Depends(get_db)): # This endpoint retrieves all blog entries
    # It uses the models.Blog model to query the database
    blog = db.query(models.Blog).all()
    return blog
         
@app.get('/blog/{id}', status_code=200,response_model = schemas.showBlog, tags = ['Blog']) # This endpoint retrieves a specific blog entry by its ID
def get_id(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog not found with id {id}")
        # Response(status_code=status.HTTP_404_NOT_FOUND) # If the blog with the given id is not found, it returns a 404 Not Found response
        # return {"error": f"Blog not found with id {id}"}
    return blog 

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Blog'])
def delete_blog(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED, tags = ['Blog'])
def update_blog(id, request: schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog not found with id {id}")
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return request.dict()  # Return the updated blog data as  a response


@app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.showUser,tags = ['User'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username, email=request.email, password=hashing.Hash.bcrypt(request.password)) 
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=schemas.showUser, tags = ['User'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found with id {id}")
    return user
