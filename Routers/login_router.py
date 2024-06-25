from fastapi import APIRouter, HTTPException, Path, Depends, status
from DataBase.dbConect import SessionLocal
from sqlalchemy.orm import Session
from Models.user import UserSchema, RequestUser, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
import Controllers.login as login
import Models.login as login_Schema
router = APIRouter()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/autentica", response_model= login_Schema.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = login.authenticate_user(login.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Utilizador ou password incorretas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes= login.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = login.create_access_token(
        data={"sub": user.username, "name": user.full_name, "roles": user.roles,"id": user.id, "id_org": user.id_org  }, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



@router.post("/autentica_teste", response_model= login_Schema.Token)
async def login_for_access_tokens(form_data: OAuth2PasswordRequestForm = Depends()):
    user = login.authenticate_user(login.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Utilizador ou password incorretas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes= login.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = login.create_access_token(
        data={"sub": user.username, "name": user.full_name, "roles": user.roles, "id": user.id, "id_org": user.id_org }, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}