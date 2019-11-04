import os
import PyPDF2

haslo=input("Podaj haslo do plikow PDF: ")
haslo2=input("Podaj haslo do deszyfrowania plikow PDF: ")

for filename in os.listdir('pdfy\\'):
    if filename.endswith('.pdf'):
        pdfFile=open('pdfy\\' + filename, 'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFile)
        pdfWriter =PyPDF2.PdfFileWriter()
        for i in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(i))
        pdfWriter.encrypt(haslo)
        pdfFile.close()
        resultPdf=open('pdfy\\' + os.path.splitext(filename)[0] + '_encrypted' + os.path.splitext(filename)[1],'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()

for filename in os.listdir('pdfy\\'):
    if "encrypted" in filename:
        pdfFile=open('pdfy\\' + filename, 'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFile,'rb')
        if pdfReader.decrypt(haslo2)==1:
            print("Plik odszyfrowany!")
        else:
            print("Zle haslo!")
    else:
        os.remove('pdfy\\' + filename)
    pdfFile.close()
        

