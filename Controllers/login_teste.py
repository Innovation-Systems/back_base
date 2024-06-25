from sqlalchemy.orm import Session
from DataBase.model import User
from Models.user import UserSchema
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from Models.login import UserInDB, TokenData, User, Token
from Models.user import UserSchema
import Controllers.user as UserLogin
from datetime import datetime, timedelta
from fastapi import FastAPI,Depends, FastAPI, HTTPException, status, Request
from typing import Union
from sqlalchemy.orm import Session
from DataBase.dbConect import SessionLocal

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

SECRET_KEY = "32ad6a2457c76e6efce0ea4b956c0d352fcb31235fe000c93509a6a029856235"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "carlos@teste.pt": {
        "username": "carlos@teste.pt",
        "full_name": "Carlos Mota",
        "email": "carlos@teste.pt",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
        "roles": ["admin","tecnico"],
    },
    "julio@teste.pt": {
        "username": "julio@teste.pt",
        "full_name": "Julio Matos",
        "email": "julio@teste.pt",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
        "roles": ["tecnico"],
    }
 
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="autentica")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db,  username: str, password: str):
    user = get_user(fake_db, username)
    # db:Session=Depends(get_db)

    # user = UserLogin.get_user_login(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Utilizador não activo")
    return current_user