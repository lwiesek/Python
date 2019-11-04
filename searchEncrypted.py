import os
import PyPDF2

passwd=input("Password to decrypt: ")

for filename in os.listdir('pdfy\\'):
    if filename.endswith('.pdf'):
        pdfFile=open('pdfy\\' + filename,'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFile)
        pdfWriter=PyPDF2.PdfFileWriter()
        if pdfReader.isEncrypted:
            pdfReader.decrypt(passwd)
            for pageNum in range(pdfReader.numPages):
                pageObj=pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

            pdfOutputFile=open('pdfy\\' + os.path.splitext(filename)[0] + '_decrypted'+os.path.splitext(filename)[1],'wb')
            pdfWriter.write(pdfOutputFile)
            pdfOutputFile.close()
        pdfFile.close()
        
    
