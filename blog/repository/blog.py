from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db:Session):
    blog = db.query(models.Blog).all()
    return blog

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)  # Assuming user_id is set to 1 for simplicity
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog not found with id {id}")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog not found with id {id}")
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return request.dict()  # Return the updated blog data as  a response

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog not found with id {id}")
        # Response(status_code=status.HTTP_404_NOT_FOUND) # If the blog with the given id is not found, it returns a 404 Not Found response
        # return {"error": f"Blog not found with id {id}"}
    return blog 