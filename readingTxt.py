import openpyxl


f1=open(r'C:\Users\SG0301917\OneDrive - Sabre\Desktop\ksiazki python\errorInfo.txt','r')

wb=openpyxl.Workbook()
sheet=wb.active
w=1
for line in f1.readlines():
   sheet.cell(w,1).value=line
   w+=1

wb.save("plikiTxt.xlsx")
wb.close()




