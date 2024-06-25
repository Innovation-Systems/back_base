from datetime import datetime
from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field, EmailStr
from pydantic.generics import GenericModel
from sqlalchemy import create_engine


class Token(BaseModel):
    access_token: str
    token_type: str

  
class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    id:int
    id_org:int
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    roles: List[str]
      
class UserInDB(User):
    hashed_password: str


class Tokens(BaseModel):
    access_token: str
    token_type: str

  
class TokenDatas(BaseModel):
    username: Union[str, None] = None


class Users(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    roles: List[str]
      
class UserInDBs(User):
    hashed_password: str