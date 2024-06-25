from datetime import datetime
from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field, EmailStr
from pydantic.generics import GenericModel
from sqlalchemy import create_engine

T= TypeVar('T')


class UserSchema(BaseModel):
    id:int
    nome:str = None
    email: str = None
    password: str = None
    roles:List[str]= None
    disabled: bool= None
    id_org:int
    last_login: datetime= None
    last_update: datetime= None
    create_date:datetime=None
    uuid:str

    class Config:
        orm_mode= True

class RequestUser(BaseModel):
    parameter: UserSchema= Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
