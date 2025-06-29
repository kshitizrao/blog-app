from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm  # Importing the OAuth2PasswordRequestForm for handling login requests
from .. import schemas,database,models,token # Importing the schema module which contains the Login schema
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..token import create_access_token  # Importing the function to create JWT tokens


router = APIRouter(
    tags=['Authentication'],  # This tag is used to group the authentication-related endpoints in the API documentation
)

@router.post('/login')
def login(request : OAuth2PasswordRequestForm =Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()  # Fetch the user from the database based on the provided username (email)
    if not user:
        return HTTPException(status_code=400, detail="Invalid credentials")
    
    if not Hash.verify( request.password, user.password):
         #user.password is the hashed password stored in the database and request.password is the plain text password provided by the user.
        return HTTPException(status_code=400, detail="Incorrect password")
    # generate a JWT token and return it.
    

    access_token = token.create_access_token(data={"sub": user.email})  # Create a JWT token with the username as the subject)
    return {"access_token":access_token, "token_type":"bearer"}
    



 
