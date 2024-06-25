import pdfplumber

with pdfplumber.open("/home/server/app/PU2022.pdf") as pdf:
    first_page = pdf.pages[5]
    print(first_page.chars)