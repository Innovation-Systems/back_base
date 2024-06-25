from datetime import datetime
from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field, EmailStr
from pydantic.generics import GenericModel
from sqlalchemy import create_engine

T= TypeVar('T')


class Logs_SistemaSchema(BaseModel):
    id_log:int
    tabela:str=None
    acao:str=None
    uuid_campo:str=None
    acao_date:datetime=None
    id:int
    uuid:str=None


    class Config:
        orm_mode= True

class RequestLogs_Sistema(BaseModel):
    parameter: Logs_SistemaSchema= Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
