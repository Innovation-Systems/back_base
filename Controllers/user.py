from sqlalchemy.orm import Session
from DataBase.model import User
from Models.user import UserSchema
from Models.logs_sistema import Logs_SistemaSchema
import Controllers.login as login
import Controllers.log_sistema as logs
import uuid
import hashlib
import datetime

# get user

async def get_user(db: Session, token:str, skipt: int = 0, limit: int = 100):
    return db.query(User).offset(skipt).limit(limit).all()
  
# get user pelo id

def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_login(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()

def get_user_idOrg(db: Session, org_id: int):
    return db.query(User).filter(User.id_org == org_id).order_by(User.id).all()

# criar novo user

def create_user(db: Session, user: UserSchema):

    password_hash=hashlib.md5(user.password.encode('utf-8')).hexdigest()
    uuid_gerado= uuid.uuid4()

    _user = User(nome=user.nome, email=user.email,  roles=user.roles,
                 password=password_hash , disabled=user.disabled, last_login=user.last_login, last_update=user.last_update,  id_org=user.id_org , uuid=uuid_gerado)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user
    
# remover user

def remove_user(db: Session, user_id: int):
    _user = get_user_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()

# update user

def update_user(db: Session, user: User):
    _user = get_user_id(db=db, user_id=user.id)
    _user.nome = user.nome
    _user.email = user.email
    _user.roles= user.roles
    _user.disabled=user.disabled
    db.commit()
    db.refresh(_user)
    return _user

def update_user_password(db: Session, id: int, password:str ):
    _user = get_user_id(db=db, user_id=id)
    _user.password = hashlib.md5(password).hexdigest()
    db.commit()
    db.refresh(_user)
    return _user
