from PyPDF2 import PdfReader

reader = PdfReader("IE_510343333 (2).pdf")
number_of_pages = len(reader.pages)
page = reader.pages[1]
text = page.extract_text()
print(text)