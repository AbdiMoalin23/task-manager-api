from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException

from app.models import User
from app import schemas
from app.database import SessionLocal

SECRET_KEY = "this-is-my-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #OAuth2 Dependency object

pwd_context = CryptContext(#Hashing Tool
    schemes=["bcrypt"],
    deprecated = "auto"
)

def hash_password(password): #Hashing password function
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify_password(password, hashed_password): #Verifying password & hashed password match
    return pwd_context.verify(password, hashed_password)

def create_access_token(data): #Generates JWT token
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        
        db = SessionLocal()
        user = db.query(User).filter(User.email == email).first()

        if user is None:
            raise HTTPException(status_code=401, detail="User is not found")
        
        return user
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    
    
