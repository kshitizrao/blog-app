from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..import schemas, models,database,oauth2
from ..repository import blog

router = APIRouter(
    tags=['Blogs'], # This tag is used to group the blog-related endpoints in the API documentation
    prefix = '/blog' # This prefix is used to define the base path for all blog-related endpoints
)

@router.get('/', response_model=List[schemas.showBlog]) # This endpoint retrieves all blog entries
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)): # This endpoint retrieves all blog entries
    # It uses the models.Blog model to query the database
    return blog.get_all(db)  # This calls the get_all function from the blog repository to fetch all blogs

@router.post('/', status_code=status.HTTP_201_CREATED) # This endpoint uses the schemas.Blog model
def create(request: schemas.Blog, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)  # This calls the create function from the blog repository to create a new blog entry

@router.get('/{id}', status_code=200,response_model = schemas.showBlog) # This endpoint retrieves a specific blog entry by its ID
def get_id(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
# This calls the show function from the blog repository to fetch a blog entry by its ID 

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)
    # This calls the delete function from the blog repository to delete a blog entry by its ID

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
    # This calls the update function from the blog repository to update a blog entry by its ID 