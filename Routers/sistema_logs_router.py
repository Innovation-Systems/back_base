from fastapi import APIRouter, HTTPException, Path, Depends, UploadFile
from DataBase.dbConect import SessionLocal
from sqlalchemy.orm import Session
from Models.user import UserSchema, RequestUser, Response
from Models.logs_sistema import Logs_SistemaSchema, RequestLogs_Sistema, Response
import Controllers.log_sistema as logs
import Controllers.user as user
import Controllers.login as login
import Models.login as login_Schema
from typing import List, Optional, Generic, TypeVar, Union

router = APIRouter()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/get_all_logs')
async def get_log(db:Session=Depends(get_db),current_user: login_Schema.User = Depends(login.get_current_active_user)):
   _log= logs.get_logs(db, 0, 100)
   return Response (code=200, status="ok", message=" Fetch com sucesso", result=_log ).dict(exclude_none=True)

@router.get('/get_log_idUser/{id}')
async def get_log_idUser( id: int, db:Session=Depends(get_db),current_user: login_Schema.User = Depends(login.get_current_active_user) ):
    _log= logs.get_log_user(db, id)
    return Response (code=200, status="ok", message=" Fetch com sucesso", result=_log ).dict(exclude_none=True)