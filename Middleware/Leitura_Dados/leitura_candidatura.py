from PyPDF2 import PdfReader
from fastapi import APIRouter, HTTPException, Path, Depends, UploadFile
from typing import List, Optional, Generic, TypeVar, Union
from sqlalchemy.orm import Session
import Models.login as login_Schema
import tabula
import csv
  
# creating a pdf file object
#pdfFileObj = open('/home/pdpm19/Desktop/Babel/Iban.pdf', 'rb')

async def leitura_candidatura(db:Session,  user:login_Schema.User, file:Union[UploadFile, None]=None,):
    dfs = tabula.read_pdf(file.file, pages='all')[10]


    # convert PDF into CSV file
    f = tabula.convert_into(file.file, file.filename+".csv", output_format="csv", pages='all')
    dfs.to_csv( file.filename+"t.csv")

    # Ler o csv
    csvText = []
    with open("/home/server/app/"+file.filename+".csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
        # Procura o cabeçalho
            csvText.append(row)

    # # Print só para ver o que está a fazer
    for row in csvText:
       print(row)