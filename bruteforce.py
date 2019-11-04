import PyPDF2

f=open('dictionary.txt','r')
lista=[]
for x in f:
    lista.append(x)

for i in range(len(lista)):
    lista[i]=lista[i].rstrip()


pdfFile=open('pdfy\\meetingminutes_encrypted.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFile)

for x in lista:
    if (pdfReader.decrypt(x) ==1 or pdfReader.decrypt(x.lower()) ==1):
        print("PDF odszyfrowany a haslo to: " + x)
        break
    else:
        continue


    
