import os
os.chdir('/Users/btdrew/Desktop/docs-pdf')
import PyPDF2
pdfFile = open('meetingminutes1.pdf', 'rb') # opened in read binary mode
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())
# to get all the text in the doc
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())


