from sqlalchemy.orm import Session
from DataBase.model import Sistemas_logs
from Models.logs_sistema import Logs_SistemaSchema
import uuid
import datetime

# get all Logs do sistema
def get_logs(db: Session, skipt: int = 0, limit: int = 900):
    return db.query(Sistemas_logs).order_by(Sistemas_logs.id_log).all()


# get log id utilizador
def get_log_user(db: Session, id_user:int):
    return db.query(Sistemas_logs).filter(Sistemas_logs.id == id_user).all()


# criar novo logo do sistema
async def create_log(db: Session, log: Logs_SistemaSchema):
    uuid_gerado= uuid.uuid4()

    _log = Sistemas_logs( tabela=log.tabela, acao=log.acao, uuid_campo=log.uuid_campo,
                    acao_date=datetime.datetime.now(), id=log.id, uuid=uuid_gerado)

    db.add(_log)
    db.commit()
    db.refresh(_log)
    return _log
