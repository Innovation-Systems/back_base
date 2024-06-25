from sqlalchemy.orm import Session
from DataBase.model import Registo_opera_fertil_cabecalho
from Models.Registo_opera_fertil_cabecalho import Registo_opera_fertil_cabecalhoSchema
from sqlalchemy import and_
import uuid
import datetime
from fastapi import FastAPI, HTTPException



def get_all(db:Session, skipt: int= 0, limit:int= 100):
    return db.query(Registo_opera_fertil_cabecalho).offset(skipt).limit(limit).all()

def get_by_id(db:Session, _id:int):
    return db.query(Registo_opera_fertil_cabecalho).filter(Registo_opera_fertil_cabecalho.id_registo_fertil_cabecalho==_id).first()

def get_by_id_rosto(db:Session, _id:int):
    return db.query(Registo_opera_fertil_cabecalho).filter(Registo_opera_fertil_cabecalho.id_rosto==_id).all()

def new_regist(db:Session, object:Registo_opera_fertil_cabecalhoSchema):
    uuid_gerado= uuid.uuid4().hex
    _new=Registo_opera_fertil_cabecalho(

        zona_homo=object.zona_homo,
        n_sequencia=object.n_sequencia,
        n_subparcela=object.n_subparcela,
        area=object.area,
        metodo_rega=object.metodo_rega,
        cultura=object.cultura,
        compasso=object.compasso,
        porta_enxerto=object.porta_enxerto,
        n_planta=object.n_planta,
        data_plantacao=object.data_plantacao,
        produca_total=object.produca_total,
        obtida=object.obtida,

        id_rosto=object.id_rosto,
        last_update= datetime.datetime.now(), 
        create_date= datetime.datetime.now(), 
        uuid= uuid_gerado

    )

    db.add(_new)
    db.commit()
    db.refresh( _new)
    return _new


def update_regist(db:Session, object:Registo_opera_fertil_cabecalhoSchema):

    _regist_edit=get_by_id(db=db, _id=object.id_registo_fertil_cabecalho)

  
    _regist_edit.zona_homo=object.zona_homo
    _regist_edit.n_sequencia=object.n_sequencia
    _regist_edit.n_subparcela=object.n_subparcela
    _regist_edit.area=object.area
    _regist_edit.metodo_rega=object.metodo_rega
    _regist_edit.cultura=object.cultura
    _regist_edit.compasso=object.compasso
    _regist_edit.porta_enxerto=object.porta_enxerto
    _regist_edit.n_planta=object.n_planta
    _regist_edit.data_plantacao=object.data_plantacao
    _regist_edit.produca_total=object.produca_total
    _regist_edit.obtida=object.obtida
    _regist_edit.last_update= datetime.datetime.now(),

    db.commit()
    db.refresh(_regist_edit)
    return _regist_edit

def remove(db:Session, _id:int):
    _remove = get_by_id(db, _id)

    if _remove==None:
        raise HTTPException(status_code=404, detail="Erro ao Eliminar objecto %_id")
    
    db.delete(_remove)
    db.commit()