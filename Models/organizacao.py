from datetime import datetime
from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field, EmailStr
from pydantic.generics import GenericModel
from sqlalchemy import create_engine

T= TypeVar('T')


class OrganizationSchema(BaseModel):
    id:int
    nome:str =None
    morada: str =None
    nif: str =None
    logo:str=None
    logo1:str=None
    logo2:str=None
    responsavel:str =None
    disabled: bool =None
    create_date: datetime =None
    last_update: datetime =None
    uuid:str

    class Config:
        orm_mode= True

class RequestOrganization(BaseModel):
    parameter: OrganizationSchema= Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]