from sqlalchemy.orm import Session
from PyPDF2 import PdfReader
from fastapi import APIRouter, HTTPException, Path, Depends, UploadFile
from typing import List, Optional, Generic, TypeVar, Union
import tabula
import csv
import Controllers.parcelas as parcelasB
import Controllers.agricultor as agricultor
from Models.parcelas import ParcelasSchema
from Models.agricultor import AgricultorSchema
import Models.login as login_Schema

  
# creating a pdf file object
#pdfFileObj = open('/home/pdpm19/Desktop/Babel/Iban.pdf', 'rb')

lista = [['Seq', '', '', 'Finanças', '', 'Forma S/N/L', '(ha)', '1o PILAR 2o PILAR', 'atualização'], ['Forma','S/N/L','1o PILAR','2o PILAR','','','','','','','','']]

async def leitura_IE(db:Session,  user:login_Schema.User, file:Union[UploadFile, None]=None,):

    print (file.filename)
    # # creating a pdf reader object
    
    pdf = PdfReader(file.file)
    page = pdf.pages[0]

    text = page.extract_text()


    # Nome
    index = text.find("Nome/Designação social:")
    starting_index = index+24
    ending_index = starting_index
    for i in text[starting_index:]:
        if i == "\n":
            break
        ending_index+=1

    nome = text[index+24:ending_index]

# NIF
    index = text.find("NIF:")
    starting_index = index+5
    ending_index = starting_index
    for i in text[starting_index:]:
        if i == "N":
            break
        ending_index+=1
    nif = text[starting_index:ending_index]

# NIFAP
    index = text.find("NIFAP :")
    starting_index = index+8
    ending_index = starting_index
    for i in text[starting_index:]:
        if i == "N":
            break
        ending_index+=1
    nifap = text[starting_index:ending_index]
    

    veri=agricultor.get_agricultor_nif(db=db, agricultor_nif=nif)

    if(veri==None):

        agri:AgricultorSchema=AgricultorSchema(
            id_agri=0,
            nome=nome,
            email="",
            telefone=0,
            telemovel=0,
            morada="",
            Concelho="",
            freguesia="",
            Codigo_postal="",
            nif=nif,
            ifap=nifap,
            disabled=False,
            last_update=None,
            create_date=None,
            id_org=user.id_org,
            uuid="",
        )
        id_agricultorN=agricultor.create_agricultor(db=db ,agricultor=agri)
    
    else:
        return

# N parcelas
    n_parcelas = 0

    paginas=1
    while True:
        page = pdf.pages[paginas]
        text = page.extract_text()
        index = text.find("Nº Parcelas:")
    
        if index != -1:
            starting_index = index+14
            ending_index = starting_index
            for i in text[starting_index]:
                if i == ' ':
                    break
            ending_index += 1
            n_parcelas = int(text[starting_index:ending_index+2])
            break
        paginas +=1


    print("---------PPP---------------")
    print(n_parcelas)
    print(id_agricultorN.id_agri)
    print("-----------PPP-------------")

    """**Vai buscar as parcelas**"""

    # Read pdf into list of DataFrame
    dfs = tabula.read_pdf(file.file, pages='all')


    # convert PDF into CSV file
    f = tabula.convert_into(file.file, file.filename+".csv", output_format="csv", pages='all')

    # Ler o csv
    csvText = []
    with open("/home/server/app/"+file.filename+".csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
        # Procura o cabeçalho
            csvText.append(row)

    # # Print só para ver o que está a fazer
    # for row in csvText:
    #   print(row)


    # Cabeçalho, pois queres o que está abaixo disto
    #headerList = ['Seq', '', '', 'Finanças', '', 'Forma S/N/L', '(ha)', '1o PILAR 2o PILAR', 'atualização']
    headerIndex=[]
    
    for ind in lista:
        try:
            headerIndex = csvText.index(ind)
            break

        except:
            continue
        
    
    # Aqui entra o valor, sabido à priori do nº de entradas...
    #textoImportante = csvText[headerIndex+1:headerIndex+1+n_parcelas]

    indexP=1
    parcelas=1

    #  elimina todas as linhas que não sao necessarias nas parelas
    print ("----------")
    while True:
        if n_parcelas < parcelas:
            break
        try:
            for row in csvText[headerIndex+indexP]:
                try:
                    if int(row) != parcelas:
                        indexP+=1
                        break
                    else:
                        print(csvText[headerIndex+indexP])
                        print(csvText[headerIndex+indexP][0])
                        print(csvText[headerIndex+indexP][1])
                        parce:ParcelasSchema=ParcelasSchema(
                                id_parcelas=0,
                                numero_seq= int(csvText[headerIndex+indexP][0]),
                                numero_Parce=csvText[headerIndex+indexP][1],
                                nome=csvText[headerIndex+indexP][2],
                                seccao_finan="",
                                artigo="",
                                forma="",
                                s_n_l="",
                                multiDec="",
                                area_gis=csvText[headerIndex+indexP][8],
                                primeiro_pilar="",
                                segundo_pilar="",
                                iqfp=0,
                                acao="",
                                Data_ultima_atualizacao=None,
                                id_agri=id_agricultorN.id_agri,
                                last_update=None,
                                create_date=None,
                                uuid="",

                        )
                        await parcelasB.create_parcela(db=db,parcela=parce)
                        parcelas+=1
                        indexP+=1
                        break
                except:
                    indexP+=1
                    break
        except:
            agricultor.remove_agricultor(db=db,agricultor_id=id_agricultorN.id_agri)
    


    '''
    for row in textoImportante:
    print(row)
    '''

    """**Output esperado**"""

    print('Nome:', nome)
    print('NIF:', nif)
    print('NIFAP:', nifap)
    print('Entradas:')
    # for row in textoImportante:
    #   print(row)