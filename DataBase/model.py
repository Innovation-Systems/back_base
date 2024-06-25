import email
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Float, ForeignKey,ARRAY,Date
from  DataBase.dbConect import Base, engine



class Organization(Base):
    __tablename__='Organization'

    id_org = Column(Integer, primary_key=True, autoincrement=True)
    nome= Column(String)
    morada=Column(String)
    nif=Column(String)
    logo=Column(String)
    logo1=Column(String)
    logo2=Column(String)
    responsavel=Column(String)
    disabled = Column(Boolean)
    create_date= Column(DateTime)
    last_update= Column(DateTime)
    uuid= Column(String)

class User(Base):
    __tablename__= 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome= Column(String)
    email= Column(String)
    password= Column(String)
    roles=Column(ARRAY(String))
    disabled = Column(Boolean)
    id_org=Column(Integer, ForeignKey("Organization"))
    last_login= Column(DateTime)
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Agricultor(Base):
    __tablename__= 'Agricultor'

    id_agri = Column(Integer, primary_key=True, autoincrement=True)
    nome= Column(String)
    email= Column(String)
    telefone= Column(Integer)
    telemovel=Column(Integer)
    morada=Column(String)
    Concelho=Column(String)
    freguesia=Column(String)
    Codigo_postal=Column(String)
    nif=Column(String)
    nifap=Column(String)
    disabled = Column(Boolean)
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    id_org=Column(Integer, ForeignKey("Organization"))
    uuid= Column(String)

class Parcelas(Base):
    __tablename__='Parcelas'

    id_parcela = Column(Integer, primary_key=True, autoincrement=True)
    numero_seq=Column(Integer)
    numero_Parce=Column(String)
    nome=Column(String)
    seccao_finan=Column(String)
    artigo=Column(String)
    forma=Column(String)
    s_n_l=Column(String)
    multiDec=Column(String)
    area_gis=Column(String)
    primeiro_pilar=Column(String)
    segundo_pilar=Column(String)
    iqfp=Column(Integer)
    acao=Column(String)
    Data_ultima_atualizacao=Column(Date)
    id_agri=Column(Integer, ForeignKey("Agricultor"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Template(Base):
    __tablename__='Template'

    id_template=Column(Integer, primary_key=True, autoincrement=True)
    nome= Column(String)
    descricao= Column(String)
    id_org=Column(Integer, ForeignKey("Organization"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Template_pecuario(Base):
    __tablename__='Template_pecuario'

    id_template=Column(Integer, primary_key=True, autoincrement=True)
    nome= Column(String)
    descricao= Column(String)
    id_org=Column(Integer, ForeignKey("Organization"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Rosto_Caderno(Base):
    __tablename__='Rosto_Caderno'

    id_rosto=Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    nif=Column(String)
    nifap=Column(String)
    morada=Column(String)
    codig_postal=Column(String)
    localizacao=Column(String)
    concelho=Column(String)
    freguesia=Column(String)
    telefone=Column(Integer)
    telemovel=Column(Integer)
    email=Column(String)

    cargo=Column(String)
    nome_S=Column(String)
    morada_S=Column(String)
    telefone_S=Column(Integer)
    telemovel_S=Column(Integer)
    email_S=Column(String)
 


    local_sede_E=Column(String)
    codigo_postal_E=Column(String)
    freguesia_E=Column(String)
    concelho_E=Column(String)

    designacao_baldio=Column(String)
    n_parcelario=Column(String)
    n_subparcela=Column(String)
    localizacao_baldio=Column(String)
    concelho_baldio=Column(String)
    freguesia_baldio=Column(String)

    area_manutencao_AB=Column(String)
    area_conversao_AB=Column(String)
    area_PRODI=Column(String)
    area_total_exploracao=Column(String)
    transformacao=Column(Boolean)
    tranform_obs=Column(String)

    regante_classe_A=Column(Boolean)
    regante_classe_B_plus=Column(Boolean)
    regante_classe_B=Column(Boolean)
    area_regada=Column(String)
    titulo_regante=Column(String)
    data_contrato_ERR=Column(String)

    bovinos_conversao_AB=Column(String)
    bovinos_manutencao_AB=Column(String)
    ovinos_conversao_AB=Column(String)
    ovinos_manutencao_AB=Column(String)
    caprinos_conversao_AB=Column(String)
    caprinos_manutencao_AB=Column(String)

    outras_espe_conver_AB=Column(String)
    outras_esp_manu_AB=Column(String)
    bovinos_PRODI=Column(String)
    ovinos_PRODI=Column(String)
    caprinos_PRODI=Column(String)
    outras_esp_PRODI=Column(String)

    assistencia_tec_AB=Column(String)
    assistencia_tec_PRODI=Column(String)
    assistencia_tec_past_permanente=Column(String)
    indentificacao_OC_AB=Column(String)
    indentificacao_OC_PRODI=Column(String)
    indentificacao_OC_PP_biod=Column(String)
    identificacao_ERR=Column(String)

    drap=Column(String)
    ano=Column(Integer)

    activo=Column(Integer)
    id_agri=Column(Integer, ForeignKey("Agricultor"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Caraterizacao(Base):
    __tablename__='Caraterizacao'

    id_cara=Column(Integer, primary_key=True, autoincrement=True)
    parcela_numero=Column(Integer)
    sub_parcela=Column(Integer)
    zona_homogenea=Column(String)
    modo_producao=Column(String)
    intervencao_PEPAC=Column(String)
    area=Column(Float)
    textura_solo=Column(String)
    cultura=Column(String)
    sucessao_cultural=Column(String)
    iqfp=Column(String)
    boas_praticas=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Caraterizacao_pecuario(Base):
    __tablename__='Caraterizacao_pecuario'

    id_cara_pecu=Column(Integer, primary_key=True, autoincrement=True)
    epecie=Column(String)
    grupo_homoge=Column(String)
    classe_etaria=Column(String)
    modo_producao=Column(String)
    naturais=Column(String)
    normais=Column(String)
    finalidade_producao=Column(String)
    observacoes=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



class Registo_fitossanitaria_cabecalho(Base):

    __tablename__='Registo_fitossanitaria_cabecalho'

    id_registo_fitocabe=Column(Integer, primary_key=True, autoincrement=True)
    
    zona_homo=Column(String)
    area=Column(Float)
    tipo_rega=Column(String)
    cultura=Column(String)
    compasso=Column(String)
    producao_total=Column(String)
    esperada=Column(String)
    obtidas=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_fitossanitaria(Base):
    __tablename__='Registo_fitossanitaria'

    id_registo_fito=Column(Integer, primary_key=True, autoincrement=True)

    data=Column(Date)
    estado_fenologico=Column(String)
    inimigo=Column(String)
    metodologia=Column(String)
    estimativa_risco=Column(String)
    justifi_intervencao=Column(String)
    observacoes_aux=Column(String)
    n_autorizacao=Column(String)
    nome_biocida=Column(String)
    concentracao_dose=Column(String)
    volume_aplicacao=Column(String)
    area_tratada=Column(String)
    n_aplicador=Column(String)
    nome=Column(String)
    n_autorizacao_atividade=Column(String)
    observacoes=Column(String)

    id_registo_fitocabe=Column(Integer, ForeignKey("Registo_fitossanitaria_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_operacoes_culturais_cabecalho(Base):
    __tablename__='Registo_operacoes_culturais_cabecalho'
    id_regsto_oper_cult_cabecalho=Column(Integer, primary_key=True, autoincrement=True)

    zona_homo=Column(String)
    conversao=Column(String)
    c_1=Column(Boolean)
    c_2=Column(Boolean)
    c_3=Column(Boolean)
    area=Column(Float)

    cultura=Column(String)
    compasso=Column(String)
    porta_enxerto=Column(String)
    n_plantas=Column(Integer)
    metodo_rega=Column(String)
    date_platacao=Column(String)
    c_e=Column(String)

    producao_total=Column(String)
    esperada=Column(String)
    obtida=Column(String)
    n_contador=Column(String)
    leitura_contador_preimeira=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



class Registo_operacoes_culturais(Base):
    __tablename__='Registo_operacoes_culturais'

    id_regsto_oper_cult=Column(Integer, primary_key=True, autoincrement=True)

    data=Column(Date)
    operacao_cultural=Column(String)
    ferilizante_utili=Column(String)
    modo_aplicacao=Column(String)
    t=Column(String)
    m=Column(String)
    n=Column(String)
    po=Column(String)
    k2o=Column(String)
    mgo=Column(String)
    cao=Column(String)
    so=Column(String)
    inter_processos=Column(String)
    material_utilizado=Column(String)
    observacoes_objetivo=Column(String)
    debito_dia=Column(String)
    processo=Column(String)
    quantificacao=Column(String)

    obs=Column(String)

    id_regsto_oper_cult_cabecalho=Column(Integer, ForeignKey("Registo_operacoes_culturais_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_opera_fertil_cabecalho(Base):
    __tablename__='Registo_opera_fertil_cabecalho'
    
    id_registo_fertil_cabecalho=Column(Integer, primary_key=True, autoincrement=True)

    zona_homo= Column(String)
    n_sequencia= Column(String)
    n_subparcela= Column(String)
    area= Column(Float)
    metodo_rega= Column(String)
    cultura= Column(String)
    compasso= Column(String)
    porta_enxerto= Column(String)
    n_planta= Column(String)
    data_plantacao= Column(Date)
    produca_total= Column(String)
    obtida= Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



class Registo_opera_fertil(Base):
    __tablename__='Registo_opera_fertil'

    id_registo_fertil=Column(Integer, primary_key=True, autoincrement=True)


    data= Column(Date)
    operacao= Column(String)
    fertilizante_utilizado= Column(String)
    t= Column(String)
    m= Column(String)
    n= Column(String)
    po= Column(String)
    ko= Column(String)
    mgo= Column(String)
    cao= Column(String)
    so= Column(String)
    b= Column(String)
    camp_opcao= Column(String)


    id_registo_fertil_cabecalho=Column(Integer, ForeignKey("Registo_opera_fertil_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_opera_fertil_table2(Base):
    __tablename__='Registo_opera_fertil_table2'

    id_registo_fertil_two=Column(Integer, primary_key=True, autoincrement=True)

    elementos_forn_solo_n= Column(String)
    elementos_forn_agua_n= Column(String)
    totais_aplicados_zona_n= Column(String)
    totais_aplicados_hectare_n= Column(String)

    elementos_forn_solo_po= Column(String)
    elementos_forn_agua_po= Column(String)
    totais_aplicados_zona_po= Column(String)
    totais_aplicados_hectare_po= Column(String)

    elementos_forn_solo_ko= Column(String)
    elementos_forn_agua_ko= Column(String)
    totais_aplicados_zona_ko= Column(String)
    totais_aplicados_hectare_ko= Column(String)

    elementos_forn_solo_mgo= Column(String)
    elementos_forn_agua_mgo= Column(String)
    totais_aplicados_zona_mgo= Column(String)
    totais_aplicados_hectare_mgo= Column(String)

    elementos_forn_solo_cao= Column(String)
    elementos_forn_agua_cao= Column(String)
    totais_aplicados_zona_cao= Column(String)
    totais_aplicados_hectare_cao= Column(String)

    elementos_forn_solo_so= Column(String)
    elementos_forn_agua_so= Column(String)
    totais_aplicados_zona_so= Column(String)
    totais_aplicados_hectare_so= Column(String)

    elementos_forn_solo_b= Column(String)
    elementos_forn_agua_b= Column(String)
    totais_aplicados_zona_b= Column(String)
    totais_aplicados_hectare_b= Column(String)

    elementos_forn_solo_ob= Column(String)
    elementos_forn_agua_ob= Column(String)
    totais_aplicados_zona_ob= Column(String)
    totais_aplicados_hectare_ob= Column(String)

    id_registo_fertil_cabecalho=Column(Integer, ForeignKey("Registo_opera_fertil_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)




# 5B
class Registo_atividades_Cabecalho(Base):
    __tablename__='Registo_atividades_Cabecalho'

    id_registo_activi=Column(Integer, primary_key=True, autoincrement=True)

    zona_homo= Column(String)
    n_sequencia= Column(String)
    n_subparcela= Column(String)
    area= Column(Float)
    cultura= Column(String)
    esperada= Column(String)
    obtida= Column(String)
    data= Column(Date)
    profundidade=Column(Integer)
    data_emissao=Column(Date)
    n_amostras= Column(Integer)
    n_boletim= Column(String)


    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)




class  Registo_atividades_analises_terras(Base):
    __tablename__='Registo_atividades_analises_terras'

    id_registo_analise=Column(Integer, primary_key=True, autoincrement=True)


    mg_camp1= Column(String)
    mg_camp2= Column(String)
    mg_camp3= Column(String)
    mg_camp4= Column(String)
    mg_camp5= Column(String)
    mg_camp6= Column(String)
  

    percentagem_camp1= Column(String)
    percentagem_camp2= Column(String)
    percentagem_camp3= Column(String)
    percentagem_camp4= Column(String)
    percentagem_camp5= Column(String)
    percentagem_camp6= Column(String)
   

    Resultados_analicesPH= Column(String)
    Resultados_analicesMO= Column(String)

    fertilizacao_camp1= Column(String)
    fertilizacao_camp2= Column(String)
    fertilizacao_camp3= Column(String)
    fertilizacao_camp4= Column(String)
    fertilizacao_camp5= Column(String)
    fertilizacao_camp6= Column(String)
    fertilizacao_camp7= Column(String)
    fertilizacao_camp8= Column(String)

    deduzir_cálculo= Column(String)
    deduzir_cálculo_camp2= Column(String)

    azoto_mineral=Column(Boolean)
    azoto_nitrico=Column(Boolean)
    azoto_total=Column(Boolean)

    id_registo_activi=Column(Integer, ForeignKey("Registo_atividades_Cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_atividades_5b(Base):

    __tablename__='Registo_atividades_5b'

    id_atividade=Column(Integer, primary_key=True, autoincrement=True)

    data= Column(Date)
    operacao_cult= Column(String)
    fertilizacao= Column(String)
    produto_utilizado= Column(String)
    
    t= Column(String)
    n= Column(String)
    po= Column(String)
    ko= Column(String)
    mgo= Column(String)
    cao= Column(String)
    so= Column(String)
    b= Column(String)
    campp_opcao= Column(String)


    id_registo_activi=Column(Integer, ForeignKey("Registo_atividades_Cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)




class Registo_atividades_5b_two(Base):
    __tablename__ = 'Registo_atividades_5b_two'
    id_atividade_two=Column(Integer, primary_key=True, autoincrement=True)
    elementos_n= Column(String)
    elementos_po= Column(String)
    elementos_ko= Column(String)
    elementos_mgo= Column(String)
    elementos_cao= Column(String)
    elementos_so= Column(String)
    elementos_b= Column(String)
    elementos_campp_opcao= Column(String)


    totais_apli_homo_n= Column(String)
    totais_apli_homo_po= Column(String)
    totais_apli_homo_ko= Column(String)
    totais_apli_homo_mgo= Column(String)
    totais_apli_homo_cao= Column(String)
    totais_apli_homo_so= Column(String)
    totais_apli_homo_b= Column(String)
    totais_apli_homo_campp_opcao= Column(String)


    totais_apli_n= Column(String)
    totais_apli_po= Column(String)
    totais_apli_ko= Column(String)
    totais_apli_mgo= Column(String)
    totais_apli_cao= Column(String)
    totais_apli_so= Column(String)
    totais_apli_b= Column(String)
    totais_apli_campp_opcao= Column(String)

    id_registo_activi=Column(Integer, ForeignKey("Registo_atividades_Cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


#5C
class Registo_oper_culturais_PP_um_5c(Base):
    __tablename__='Registo_oper_culturais_PP_um'

    id_regis_ope_cult=Column(Integer, primary_key=True, autoincrement=True)
    zona_homo=Column(String)
    area=Column(String)
    data=Column(Date)
    especis_exis=Column(String)
    oper_cultural=Column(String)
    tipo_ferti=Column(String)
    ferti_utilizado=Column(String)
    t=Column(String)
    m=Column(String)
    n=Column(String)
    po=Column(String)
    ko=Column(String)
    mgo=Column(String)
    cao=Column(String)
    so=Column(String)
    b=Column(String)
    opcao=Column(String)

    
    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_oper_culturais_PP_dois_5c(Base):
    __tablename__='Registo_oper_culturais_PP_dois'

    id_regis_ope_cult=Column(Integer, primary_key=True, autoincrement=True)
    zona_homo=Column(String)
    parqueamento=Column(String)
    area=Column(String)
    cn_out_dez=Column(String)
    cn_ja_fev=Column(String)
    cn_mar_mai=Column(String)
    cn_jun_set=Column(String)

    cn_ha_out_dez=Column(String)
    cn_ha_ja_fev=Column(String)
    cn_ha_mar_mai=Column(String)
    cn_ha_jun_set=Column(String)
   

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


#5D
class Registo_act_fertil_azotada_5d_cabecalho(Base):

    __tablename__='Registo_act_fertil_azotada_cabecalho'
    
    
    id_act_feertil_azotada=Column(Integer, primary_key=True, autoincrement=True)


    zona_homo= Column(String)
    n_sequencia= Column(String)
    n_subparcela= Column(String)
    area= Column(Float)
    metodo_rega= Column(String)
    cultura= Column(String)
    compasso= Column(String)
    porta_enxerto= Column(String)
    n_planta= Column(String)
    data_plantacao= Column(Date)
    produca_total= Column(String)
    obtida= Column(String)
    
    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_act_fertil_azotada_um_5d(Base):

    __tablename__='Registo_act_fertil_azotada_um'

    id_registo_fertil_um=Column(Integer, primary_key=True, autoincrement=True)

    origem= Column(String)
    tipo_ferti= Column(String)
    nome_comercial=Column(String)
    especi_pecuaria= Column(String)
    data_aplica= Column(Date)
    quantidade_um= Column(String)
    teor_n=Column(String)
    quantidade_dois= Column(String)
    quantidade_tres= Column(String)
    quantidade_quatro= Column(String)
    quantidade_cinco= Column(String)

    id_act_feertil_azotada=Column(Integer, ForeignKey("Registo_act_fertil_azotada_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_act_fertil_azotada_dois_5d(Base):

    __tablename__='Registo_act_fertil_azotada_dois'

    id_registo_fertil_dois=Column(Integer, primary_key=True, autoincrement=True)


    data_rega= Column(Date)
    metodo_rega= Column(String)
    eficiencia_rega=Column(String)
    volume= Column(String)
    dotacao= Column(String)
    teor= Column(String)
    kg_n= Column(String)

    id_act_feertil_azotada=Column(Integer, ForeignKey("Registo_act_fertil_azotada_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_act_fertil_azotada_tres_5d(Base):
    __tablename__='Registo_act_fertil_azotada_tres'

    id_registo_fertil_tres=Column(Integer, primary_key=True, autoincrement=True)

    ferti_A= Column(String)
    ferti_B= Column(String)
    B_A= Column(String)

    tres_um= Column(String)
    tres_dois= Column(String)

    quatro_um_um= Column(String)
    quatro_um_dois= Column(String)
    quatro_um_tres= Column(String)
    quatro_um_quatro= Column(String)
    quatro_dois_um= Column(String)
    quatro_dois_dois= Column(String)


    id_act_feertil_azotada=Column(Integer, ForeignKey("Registo_act_fertil_azotada_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)




#table_6
class Registo_horario_rega_seis_cabecalho(Base):
    __tablename__='Registo_horario_rega_seis_cabecalho'

    id_horario_rega=Column(Integer, primary_key=True, autoincrement=True)
    zona_homo= Column(String)
    n_sequencia= Column(String)
    n_subparcela= Column(String)
    area= Column(Float)
    cenario_cli= Column(String)
    cultura= Column(String)
    data_sementeira= Column(String)
    n_contador= Column(String)
    leitura_contador_1= Column(String)
    data_plantacao= Column(Date)
    produca_total= Column(String)
    obtida= Column(String)


    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



class Registo_horario_rega_seis(Base):
    __tablename__='Registo_horario_rega_seis'

    id_registo_rega=Column(Integer, primary_key=True, autoincrement=True)
    
    capacidade_utili= Column(String)
    reserva_facilmente_utiliz= Column(String)
    eficiencia_rega= Column(String)
    mes= Column(String)
    semana_n= Column(String)

    date_camp_1= Column(String)
    date_camp_2= Column(String)
    date_camp_3= Column(String)
    date_camp_4= Column(String)
    date_camp_5= Column(String)
    date_camp_6= Column(String)
    date_camp_7= Column(String)

    prefundidad_radi_camp_1= Column(String)
    prefundidad_radi_camp_2= Column(String)
    prefundidad_radi_camp_3= Column(String)
    prefundidad_radi_camp_4= Column(String)
    prefundidad_radi_camp_5= Column(String)
    prefundidad_radi_camp_6= Column(String)
    prefundidad_radi_camp_7= Column(String)

    capacidade_campo_camp_1= Column(String)
    capacidade_campo_camp_2= Column(String)
    capacidade_campo_camp_3= Column(String)
    capacidade_campo_camp_4= Column(String)
    capacidade_campo_camp_5= Column(String)
    capacidade_campo_camp_6= Column(String)
    capacidade_campo_camp_7= Column(String)

    teor_crit_cul_camp_1= Column(String)
    teor_crit_cul_camp_2= Column(String)
    teor_crit_cul_camp_3= Column(String)
    teor_crit_cul_camp_4= Column(String)
    teor_crit_cul_camp_5= Column(String)
    teor_crit_cul_camp_6= Column(String)
    teor_crit_cul_camp_7= Column(String)

    teor_agua_inicio_camp_1= Column(String)
    teor_agua_inicio_camp_2= Column(String)
    teor_agua_inicio_camp_3= Column(String)
    teor_agua_inicio_camp_4= Column(String)
    teor_agua_inicio_camp_5= Column(String)
    teor_agua_inicio_camp_6= Column(String)
    teor_agua_inicio_camp_7= Column(String)

    eto_camp_1= Column(String)
    eto_camp_2= Column(String)
    eto_camp_3= Column(String)
    eto_camp_4= Column(String)
    eto_camp_5= Column(String)
    eto_camp_6= Column(String)
    eto_camp_7= Column(String)

    kc_camp_1= Column(String)
    kc_camp_2= Column(String)
    kc_camp_3= Column(String)
    kc_camp_4= Column(String)
    kc_camp_5= Column(String)
    kc_camp_6= Column(String)
    kc_camp_7= Column(String)

    etc_camp_1= Column(String)
    etc_camp_2= Column(String)
    etc_camp_3= Column(String)
    etc_camp_4= Column(String)
    etc_camp_5= Column(String)
    etc_camp_6= Column(String)
    etc_camp_7= Column(String)

    precipita_t_camp_1= Column(String)
    precipita_t_camp_2= Column(String)
    precipita_t_camp_3= Column(String)
    precipita_t_camp_4= Column(String)
    precipita_t_camp_5= Column(String)
    precipita_t_camp_6= Column(String)
    precipita_t_camp_7= Column(String)

    variacao_agu_camp_1= Column(String)
    variacao_agu_camp_2= Column(String)
    variacao_agu_camp_3= Column(String)
    variacao_agu_camp_4= Column(String)
    variacao_agu_camp_5= Column(String)
    variacao_agu_camp_6= Column(String)
    variacao_agu_camp_7= Column(String)

    teor_agua_solo_s_rega_camp_1= Column(String)
    teor_agua_solo_s_rega_camp_2= Column(String)
    teor_agua_solo_s_rega_camp_3= Column(String)
    teor_agua_solo_s_rega_camp_4= Column(String)
    teor_agua_solo_s_rega_camp_5= Column(String)
    teor_agua_solo_s_rega_camp_6= Column(String)
    teor_agua_solo_s_rega_camp_7= Column(String)

    leitura_sonda_1_camp_1= Column(String)
    leitura_sonda_1_camp_2= Column(String)
    leitura_sonda_1_camp_3= Column(String)
    leitura_sonda_1_camp_4= Column(String)
    leitura_sonda_1_camp_5= Column(String)
    leitura_sonda_1_camp_6= Column(String)
    leitura_sonda_1_camp_7= Column(String)

    leitura_sonda_2_camp_1= Column(String)
    leitura_sonda_2_camp_2= Column(String)
    leitura_sonda_2_camp_3= Column(String)
    leitura_sonda_2_camp_4= Column(String)
    leitura_sonda_2_camp_5= Column(String)
    leitura_sonda_2_camp_6= Column(String)
    leitura_sonda_2_camp_7= Column(String)

    folga_prox_rega_camp_1= Column(String)
    folga_prox_rega_camp_2= Column(String)
    folga_prox_rega_camp_3= Column(String)
    folga_prox_rega_camp_4= Column(String)
    folga_prox_rega_camp_5= Column(String)
    folga_prox_rega_camp_6= Column(String)
    folga_prox_rega_camp_7= Column(String)

    rega_leitura_camp_1= Column(String)
    rega_leitura_camp_2= Column(String)
    rega_leitura_camp_3= Column(String)
    rega_leitura_camp_4= Column(String)
    rega_leitura_camp_5= Column(String)
    rega_leitura_camp_6= Column(String)
    rega_leitura_camp_7= Column(String)

    rega_dose_total_camp_1= Column(String)
    rega_dose_total_camp_2= Column(String)
    rega_dose_total_camp_3= Column(String)
    rega_dose_total_camp_4= Column(String)
    rega_dose_total_camp_5= Column(String)
    rega_dose_total_camp_6= Column(String)
    rega_dose_total_camp_7= Column(String)

    rega_dose_util_camp_1= Column(String)
    rega_dose_util_camp_2= Column(String)
    rega_dose_util_camp_3= Column(String)
    rega_dose_util_camp_4= Column(String)
    rega_dose_util_camp_5= Column(String)
    rega_dose_util_camp_6= Column(String)
    rega_dose_util_camp_7= Column(String)

    teor_agua_solo_1_camp_1= Column(String)
    teor_agua_solo_1_camp_2= Column(String)
    teor_agua_solo_1_camp_3= Column(String)
    teor_agua_solo_1_camp_4= Column(String)
    teor_agua_solo_1_camp_5= Column(String)
    teor_agua_solo_1_camp_6= Column(String)
    teor_agua_solo_1_camp_7= Column(String)

    perda_agua_camp_1= Column(String)
    perda_agua_camp_2= Column(String)
    perda_agua_camp_3= Column(String)
    perda_agua_camp_4= Column(String)
    perda_agua_camp_5= Column(String)
    perda_agua_camp_6= Column(String)
    perda_agua_camp_7= Column(String)

    ident_camp1= Column(String)
    ident_camp2= Column(String)
    ident_camp3= Column(String)
    ident_camp4= Column(String)

    id_horario_rega=Column(Integer, ForeignKey("Registo_horario_rega_seis_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_producao_animal_sete_cabecalho(Base):
    __tablename__='Registo_producao_animal_sete_cabecalho'    

    id_registo_pro=Column(Integer, primary_key=True, autoincrement=True)

    especi=Column(String)
    grupo_homo=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_producao_animal_sete(Base):
    __tablename__='Registo_producao_animal_sete'    

    id_registo_pro_ani=Column(Integer, primary_key=True, autoincrement=True)

    data_camp1=Column(String)
    data_camp2=Column(String)

    justif_camp1=Column(String)
    justif_camp2=Column(String)

    alter_camp1=Column(String)
    alter_camp2=Column(String)

    alimenta_camp1=Column(String)
    alimenta_camp2=Column(String)

    operacoescamp1=Column(String)
    operacoescamp2=Column(String)

    control_camp1=Column(String)
    control_camp2=Column(String)

    prod_camp1=Column(String)
    prod_camp2=Column(String)

   
    id_registo_pro=Column(Integer, ForeignKey("Registo_producao_animal_sete_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Registo_producao_animal_obs_set(Base):
    __tablename__='Registo_producao_animal_obs_set'    

    id_registo_pro_ani_obs=Column(Integer, primary_key=True, autoincrement=True)

    obs=Column(String)

    id_registo_pro=Column(Integer, ForeignKey("Registo_producao_animal_sete_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


#tabela 8---------------------------------------------------------------------------------------------------

class Registo_pos_colheita_oito_cabecalhos(Base):
    __tablename__='Registo_pos_colheita_oito_cabecalhos' 

    id_registo_colh=Column(Integer, primary_key=True, autoincrement=True)

    zona_homo= Column(String)
    c1=Column(Boolean)
    c2=Column(Boolean)
    c3=Column(Boolean)
    area= Column(Float)
    cultura= Column(String)
    compasso= Column(String)
    porta_enxerto= Column(String)
    n_planta= Column(String)
    data_plantacao= Column(String)
    produca_total= Column(String)
    obtida= Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Registo_pos_colheita_oito(Base):
    __tablename__='Registo_pos_colheita_oito_' 

    id_registo_pos_colhe=Column(Integer, primary_key=True, autoincrement=True)

    data= Column(Date)
    embalagem=Column(String)
    quantificacao=Column(String)
    destinatario=Column(String)
    quantificacao_dois= Column(String)

    id_registo_colh=Column(Integer, ForeignKey("Registo_pos_colheita_oito_cabecalhos"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



# tabela 9---------------------------------------------------------

class Registo_adquisicao_entrada_nove(Base):
    __tablename__='Registo_adquisicao_entrada_nove'

    id_entradas=Column(Integer, primary_key=True, autoincrement=True)

    data= Column(Date)
    produto=Column(String)
    quantidade=Column(String)
    fornecedor=Column(String)
    origem=Column(String)
    destino=Column(String) 
    doc=Column(String)  
    consumo_energético=Column(String)    
    obs=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)  



#tabela 10------------------------------------------------------------
class Registo_vendas_dez(Base):
    __tablename__='Registo_vendas_dez'

    id_vendas=Column(Integer, primary_key=True, autoincrement=True)

    data=Column(Date)
    produto=Column(String)
    quantidade=Column(String)
    cliente=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


#..........................falta fazer modelos...........................

#tabela 11-----------------------------------------------------------------------
class Registo_gest_fluentes_onze_um(Base):
    __tablename__='Registo_gest_fluentes_onze_um'  

    id_fluentes_um=Column(Integer, primary_key=True, autoincrement=True)

    fossas=Column(String)
    nitreiras=Column(String)
    valas_condu_fluentes=Column(String)
    lagos_imperm=Column(String)
    outros_reservatorios=Column(String) 
    contratualizada=Column(String)



    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String) 

class Registo_gest_fluentes_onze_dois(Base):
    __tablename__='Registo_gest_fluentes_onze_dois'

    id_fluentes_dois=Column(Integer, primary_key=True, autoincrement=True)

    categoria_animal=Column(String)
    especie_animal=Column(String)
    n_animais=Column(String)
    ex_chorume=Column(String)
    ex_estrume=Column(String)
    exter_chorume=Column(String)
    exter_estrume=Column(String)
    vendido_chorume=Column(String)
    vendido_estrume=Column(String)
    quant_chorume=Column(String)
    quant_estrume=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)     


class Registo_gest_fluentes_onze_tres(Base):
    __tablename__='Registo_gest_fluentes_onze_tres'
      
    id_fluentes_tres=Column(Integer, primary_key=True, autoincrement=True)

    n_parcelario=Column(Integer)
    cultura=Column(String)
    propria=Column(Float)
    contratualizada=Column(Float)
    tipo=Column(String)
    origem=Column(String)
    data=Column(Date)
    quant=Column(Float)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Registo_anexo_um_cabecalho(Base):
    __tablename__='Registo_anexo_um_cabecalho'

    id_anexo_um_cabecalho=Column(Integer, primary_key=True, autoincrement=True)

    zona_homo= Column(String)
    n_sequencia= Column(String)
    n_subparcela= Column(String)
    area= Column(Float)
    cultura= Column(String)
    idade= Column(Float)
    producao_esperado= Column(Float)
    insta= Column(Boolean)
    manutencao= Column(Boolean)
    producao= Column(Boolean)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Registo_anexo_um_Analisses_terras(Base):
    __tablename__='Registo_anexo_um_Analisses_terras'

    id_anexo_um_um=Column(Integer, primary_key=True, autoincrement=True)

    mg_camp1=Column(String)
    mg_camp2=Column(String)
    mg_camp3=Column(String)
    mg_camp4=Column(String)
    mg_camp5=Column(String)
    mg_camp6=Column(String)

    perc_camp1=Column(String)
    perc_camp2=Column(String)
    perc_camp3=Column(String)
    perc_camp4=Column(String)
    perc_camp5=Column(String)
    perc_camp6=Column(String)

    mg_per_ph=Column(String)
    mg_per_mo=Column(String)

    classe_fert_camp1=Column(String)
    classe_fert_camp2=Column(String)
    classe_fert_camp3=Column(String)
    classe_fert_camp4=Column(String)
    classe_fert_camp5=Column(String)
    classe_fert_camp6=Column(String)
    classe_fert_camp7=Column(String)
    classe_fert_camp8=Column(String)

    deduzir_camp1=Column(String)
    deduzir_camp2=Column(String)

    Azoto_mineral=Column(Boolean)
    Azoto_mitrico=Column(Boolean)
    azoto_total=Column(Boolean)

    data_colheira=Column(Date)
    pronfundidade=Column(Float)
    data_resultados=Column(Date)
    n_amostras=Column(Float)
    n_boletin=Column(String)


    id_anexo_um_cabecalho=Column(Integer, ForeignKey("Registo_anexo_um_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Registo_anexo_um_Analisses_agua_rega(Base):
    __tablename__='Registo_anexo_um_Analisses_agua_rega'

    id_anexo_um_dois=Column(Integer, primary_key=True, autoincrement=True)

    dotacao=Column(Float)
    origem_agua=Column(String)
    metodo_rega=Column(String)
    eficiencia=Column(String)
    razao=Column(String)

    resultado_camp1=Column(String)
    resultado_camp2=Column(String)
    resultado_camp3=Column(String)
    resultado_camp4=Column(String)
    resultado_camp5=Column(String)
    resultado_camp6=Column(String)
    resultado_camp7=Column(String)
    resultado_camp8=Column(String)
    resultado_camp9=Column(String)
    resultado_camp10=Column(String)
    resultado_camp11=Column(String)

    quantidade_nutri_camp1=Column(String)
    quantidade_nutri_camp2=Column(String)
    quantidade_nutri_camp3=Column(String)

    k=Column(Boolean)
    ko=Column(Boolean)

    data_colheita=Column(Date)
    data_resultados=Column(Date)
    n_amostras=Column(Float)
    n_boletin=Column(String)

    id_anexo_um_cabecalho=Column(Integer, ForeignKey("Registo_anexo_um_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



class Registo_anexo_um_Analisses_foliar(Base):
    __tablename__='Registo_anexo_um_Analisses_foliar'

    id_anexo_um_tres=Column(Integer, primary_key=True, autoincrement=True)

    resultado_camp1=Column(String)
    resultado_camp2=Column(String)
    resultado_camp3=Column(String)
    resultado_camp4=Column(String)
    resultado_camp5=Column(String)
    resultado_camp6=Column(String)
    resultado_camp7=Column(String)
    resultado_camp8=Column(String)
    resultado_camp9=Column(String)
    resultado_camp10=Column(String)
    resultado_camp11=Column(String)

    classificacao_camp1=Column(String)
    classificacao_camp2=Column(String)
    classificacao_camp3=Column(String)
    classificacao_camp4=Column(String)
    classificacao_camp5=Column(String)
    classificacao_camp6=Column(String)
    classificacao_camp7=Column(String)
    classificacao_camp8=Column(String)
    classificacao_camp9=Column(String)
    classificacao_camp10=Column(String)
    classificacao_camp11=Column(String)

    data_colheita=Column(Date)
    data_resultados=Column(Date)
    n_amostras=Column(Float)
    n_boletin=Column(String)

    id_anexo_um_cabecalho=Column(Integer, ForeignKey("Registo_anexo_um_cabecalho"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)




#-------estou aqui a rever-------------------------------


#__________________________________________________________________________________

#__________________________________________________________________________________

#__________________________velhas tabelas__________________________________________


class Zona_homogenea(Base):
    __tablename__='Zona_homogenea'

    id_zona_homo=Column(Integer, primary_key=True, autoincrement=True)

    zona_homo=Column(String)
    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))


    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Zona_homogenea_pecuario(Base):
    __tablename__='Zona_homogenea_pecuario'

    id_zona_homo=Column(Integer, primary_key=True, autoincrement=True)

    zona_homo=Column(String)
    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))


    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)




# -----------------------base de dados velha-------------------------------

""" class Caraterizacao_zona_homogenea_rosto(Base):
    __tablename__='Caraterizacao_zona_homogenea_rosto'

    id_zona_homo_rosto=Column(Integer, primary_key=True, autoincrement=True)
    zona_homo=Column(String)
    cultura_grupo=Column(String)
    variedade=Column(String)
    c1=Column(Boolean)
    c2=Column(Boolean)
    c3=Column(Boolean)
    area=Column(Float)
    tipo_rega=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Pecuaria_grupo_homogenea(Base):
    __tablename__='Pecuaria_grupo_homogenea'

    id_grupo_homo=Column(Integer, primary_key=True, autoincrement=True)
    especie_animal=Column(String)
    grupo_homo=Column(String)
    
    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



class Caraterizacao_zona_homogenea(Base):
    __tablename__='Caraterizacao_zona_homogenea'

    id_zona_homo=Column(Integer, primary_key=True, autoincrement=True)
    data_estado_camp1=Column(String)
    data_estado_camp2=Column(String)
    just_inter_camp1=Column(String)
    just_inter_camp2=Column(String)
    just_inter_obs=Column(String)
    estimativa_risco_camp1=Column(String)
    estimativa_risco_camp2=Column(String)
    estimativa_risco_obs=Column(String)
    oper_infestantes_camp1=Column(String)
    oper_infestantes_camp2=Column(String)
    oper_infestantes_obs=Column(String)
    irrigacao_camp1=Column(String)
    irrigacao_camp2=Column(String)
    irrigacao_obs=Column(String)
    fertilizacao_camp1=Column(String)
    fertilizacao_camp2=Column(String)
    fertilizacao_obs=Column(String)
    tratamento_camp1=Column(String)
    tratamento_camp2=Column(String)
    tratamento_obs=Column(String)
    producao_camp1=Column(String)
    producao_camp2=Column(String)
    producao_obs=Column(String)
    visitas_camp1=Column(String)
    visitas_camp2=Column(String)
    visitas_obs=Column(String)

    id_zona_homo_rosto=Column(Integer, ForeignKey("Caraterizacao_zona_homogenea_rosto"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class Carate_pecuario_grupo_homo(Base):
    __tablename__='Carate_pecuario_grupo_homo'

    id_cara_grupo_homo=Column(Integer, primary_key=True, autoincrement=True)
    data=Column(String)
    animais=Column(String)
    facto_oco_diagnostico=Column(String)
    quantificacao=Column(String)
    obs_0=Column(String)
    motivo_justificado=Column(String)
    quantificacao_numero=Column(String)
    obs_1=Column(String)
    silagem_pastagens=Column(String)
    qunatificacao_homogenea=Column(String)
    obs_2=Column(String)
    tipo_inter=Column(String)
    meterial_quantificacao=Column(String)
    obs_3=Column(String)
    metodo_produto=Column(String)
    posologia=Column(String)
    obs_4=Column(String)
    designacao_embalagem=Column(String)
    quantificacao_lote_desti=Column(String)
    obs_5=Column(String)
    operador_trator=Column(String)
    n_animais_horas=Column(String)
    obs_6=Column(String)

    id_grupo_homo=Column(Integer, ForeignKey("Pecuaria_grupo_homogenea"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class AnexoI(Base):
    __tablename__='AnexoI'

    id_anexoI=Column(Integer, primary_key=True, autoincrement=True)
    data= Column(Date)
    produto=Column(String)
    quantidade=Column(String)
    origem=Column(String)
    destino=Column(String)
    doc_nun=Column(String)
    observacoes=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class AnexoII(Base):
    __tablename__='AnexoII'

    id_anexoII=Column(Integer, primary_key=True, autoincrement=True)
    produto=Column(String)
    quantidade=Column(String)
    epoca=Column(String)
    n_fornecido=Column(String)
    observacoes=Column(String)
    camp1=Column(String)
    camp2=Column(String)
    camp3=Column(String)
    camp4=Column(String)
    camp5=Column(String)
    camp6=Column(String)
    camp7=Column(String)
    camp8=Column(String)
    des_produto=Column(String)
    quantidade_dois=Column(String)
    n_1=Column(String)
    p_1=Column(String)
    k_1=Column(String)
    ca_1=Column(String)
    mg_1=Column(String)
    micro_1=Column(String)
    n_2=Column(String)
    p_2=Column(String)
    k_2=Column(String)
    ca_2=Column(String)
    mg_2=Column(String)
    micro_2=Column(String)
    epoca_prevista=Column(String)
    observacoes_1=Column(String)

    id_zona_homo_rosto=Column(Integer, ForeignKey("Caraterizacao_zona_homogenea_rosto"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class AnexoIII(Base):
    __tablename__='AnexoIII'

    id_anexoIII=Column(Integer, primary_key=True, autoincrement=True)
    veiculos_camp1=Column(String)
    veiculos_camp2=Column(String)
    pessoas_camp1=Column(String)
    pessoas_camp2=Column(String)
    animais_camp1=Column(String)
    animais_camp2=Column(String)
    produtos_camp1=Column(String)
    produtos_camp2=Column(String)
    centro_camp1=Column(String)
    centro_camp2=Column(String)
    control_camp1=Column(String)
    control_camp2=Column(String)
    proveniencia_camp1=Column(String)
    proveniencia_camp2=Column(String)
    plano_camp1=Column(String)
    plano_camp2=Column(String)
    contro_armaz_camp1=Column(String)
    contro_armaz_camp2=Column(String)
    lavagem_camp1=Column(String)
    lavagem_camp2=Column(String)
    limpeza_camp1=Column(String)
    limpeza_camp2=Column(String)
    vazio_camp1=Column(String)
    vazio_camp2=Column(String)
    periodicidade_camp1=Column(String)
    periodicidade_camp2=Column(String)
    destino_camp1=Column(String)
    destino_camp2=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class AnexoIV(Base):
    __tablename__='AnexoIV'

    id_anexoIV=Column(Integer, primary_key=True, autoincrement=True)
    especi_homogeneo=Column(String)
    cruzados_inter=Column(Boolean)
    cruzamentos_linha_pura=Column(Boolean)
    raca=Column(String)
    cruzamento_insdus=Column(Boolean)
    raca_pai=Column(String)
    raca_mae=Column(String)

    f_idade=Column(Boolean)
    f_estado_repro=Column(Boolean)
    f_finalidade_produ=Column(Boolean)
    f_utilizacao_parce_insta=Column(Boolean)
    f_raca=Column(Boolean)

    f_cobricao=Column(Boolean)
    f_transplante_embri=Column(Boolean)
    f_inseminacao_arti=Column(Boolean)
    f_proporcao_cobri_epoca=Column(String)

    f_sim=Column(Boolean)
    f_nao=Column(Boolean)
    f_melhor_preco=Column(Boolean)
    f_recursos=Column(Boolean)
    f_melhor_ferti=Column(Boolean)
    f_recursos_humanos=Column(Boolean)

    f_epoca_cobricao=Column(String)
    f_longevidade=Column(String)
    f_reinicio_reproducao_apos_parto=Column(String)
    f_ajuda_cuidades_re_nascidos=Column(String)
    f_assistencia_puerpe_femea=Column(String)
    f_efetivo_proveniente=Column(Boolean)
    f_adquiridos_exterior_expl=Column(Boolean)

    m_efetivo_prove_explo=Column(Boolean)
    m_adquiridos_exteri_explo=Column(Boolean)
    m_idade_inicios_repro=Column(String)
    m_peso_condicao_corporal=Column(String)
    m_avaliacao_aptidao_repro=Column(String)
    
    observacoes=Column(String)

    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)



class AnexoII_template(Base):
    __tablename__='AnexoII_template'

    id_anexoII=Column(Integer, primary_key=True, autoincrement=True)
    produto=Column(String)
    quantidade=Column(String)
    epoca=Column(String)
    n_fornecido=Column(String)
    observacoes=Column(String)
    camp1=Column(String)
    camp2=Column(String)
    camp3=Column(String)
    camp4=Column(String)
    camp5=Column(String)
    camp6=Column(String)
    camp7=Column(String)
    camp8=Column(String)
    des_produto=Column(String)
    quantidade_dois=Column(String)
    n_1=Column(String)
    p_1=Column(String)
    k_1=Column(String)
    ca_1=Column(String)
    mg_1=Column(String)
    micro_1=Column(String)
    n_2=Column(String)
    p_2=Column(String)
    k_2=Column(String)
    ca_2=Column(String)
    mg_2=Column(String)
    micro_2=Column(String)
    epoca_prevista=Column(String)
    observacoes_1=Column(String)

    id_template=Column(Integer, ForeignKey("Template"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class AnexoIII_template(Base):
    __tablename__='AnexoIII_template'

    id_anexoIII=Column(Integer, primary_key=True, autoincrement=True)
    veiculos_camp1=Column(String)
    veiculos_camp2=Column(String)
    pessoas_camp1=Column(String)
    pessoas_camp2=Column(String)
    animais_camp1=Column(String)
    animais_camp2=Column(String)
    produtos_camp1=Column(String)
    produtos_camp2=Column(String)
    centro_camp1=Column(String)
    centro_camp2=Column(String)
    control_camp1=Column(String)
    control_camp2=Column(String)
    proveniencia_camp1=Column(String)
    proveniencia_camp2=Column(String)
    plano_camp1=Column(String)
    plano_camp2=Column(String)
    contro_armaz_camp1=Column(String)
    contro_armaz_camp2=Column(String)
    lavagem_camp1=Column(String)
    lavagem_camp2=Column(String)
    limpeza_camp1=Column(String)
    limpeza_camp2=Column(String)
    vazio_camp1=Column(String)
    vazio_camp2=Column(String)
    periodicidade_camp1=Column(String)
    periodicidade_camp2=Column(String)
    destino_camp1=Column(String)
    destino_camp2=Column(String)

    id_template=Column(Integer, ForeignKey("Template"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)


class AnexoIV_template(Base):
    __tablename__='AnexoIV_template'

    id_anexoIV=Column(Integer, primary_key=True, autoincrement=True)
    especi_homogeneo=Column(String)
    cruzados_inter=Column(Boolean)
    cruzamentos_linha_pura=Column(Boolean)
    raca=Column(String)
    cruzamento_insdus=Column(Boolean)
    raca_pai=Column(String)
    raca_mae=Column(String)

    f_idade=Column(Boolean)
    f_estado_repro=Column(Boolean)
    f_finalidade_produ=Column(Boolean)
    f_utilizacao_parce_insta=Column(Boolean)
    f_raca=Column(Boolean)

    f_cobricao=Column(Boolean)
    f_transplante_embri=Column(Boolean)
    f_inseminacao_arti=Column(Boolean)
    f_proporcao_cobri_epoca=Column(String)

    f_sim=Column(Boolean)
    f_nao=Column(Boolean)
    f_melhor_preco=Column(Boolean)
    f_recursos=Column(Boolean)
    f_melhor_ferti=Column(Boolean)
    f_recursos_humanos=Column(Boolean)

    f_epoca_cobricao=Column(String)
    f_longevidade=Column(String)
    f_reinicio_reproducao_apos_parto=Column(String)
    f_ajuda_cuidades_re_nascidos=Column(String)
    f_assistencia_puerpe_femea=Column(String)
    f_efetivo_proveniente=Column(Boolean)
    f_adquiridos_exterior_expl=Column(Boolean)

    m_efetivo_prove_explo=Column(Boolean)
    m_adquiridos_exteri_explo=Column(Boolean)
    m_idade_inicios_repro=Column(String)
    m_peso_condicao_corporal=Column(String)
    m_avaliacao_aptidao_repro=Column(String)
    
    observacoes=Column(String)

    id_template=Column(Integer, ForeignKey("Template_pecuario"))    
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)
 """


class Caderno_historico(Base):
    __tablename__='Caderno_historico'

    id_caderno=Column(Integer, primary_key=True, autoincrement=True)
    ano=Column(Integer)
    link=Column(String)
    publico=Column(Boolean)
    
    id_rosto=Column(Integer, ForeignKey("Rosto_Caderno"))
    last_update= Column(DateTime)
    create_date= Column(DateTime)
    uuid= Column(String)

class Login_logs(Base):
    __tablename__='Login_logs'

    id_log=Column(Integer, primary_key=True, autoincrement=True)
    id=Column(Integer, ForeignKey("User"))
    login_date= Column(DateTime)
    uuid= Column(String)


class Sistemas_logs(Base):
    __tablename__='Sistemas_logs'

    id_log=Column(Integer, primary_key=True, autoincrement=True)
    tabela=Column(String)
    acao=Column(String)
    uuid_campo=Column(String)
    acao_date= Column(DateTime)
    id=Column(Integer, ForeignKey("User"))
    uuid= Column(String)

Base.metadata.create_all(engine)