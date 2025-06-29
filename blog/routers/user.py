from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, hashing, database

router = APIRouter(
    tags = ['user'],
    prefix = '/user'
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.showUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(username=request.username, email=request.email, password=hashing.Hash.bcrypt(request.password)) 
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.showUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found with id {id}")
    return user