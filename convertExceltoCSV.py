import os, openpyxl,csv

for excelFile in os.listdir('.'):
    if not excelFile.endswith('.xlsx'):
        continue
    wb=openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        sheet=wb[sheetName]
        csvFileObj=open(excelFile[0:len(excelFile)-5]+'_'+sheetName+'.csv','w',newline='')
        csvWriter=csv.writer(csvFileObj)
        for rowNum in range(1,sheet.max_row +1):
            rowData=[]
            for colNum in range(1,sheet.max_column +1):
                rowData.append(sheet.cell(rowNum,colNum).value)
            csvWriter.writerow(rowData)
        csvFileObj.close()

    print('Plik '+ excelFile + ' gotowy!')
                
