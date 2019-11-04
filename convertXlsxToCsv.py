import openpyxl,os,csv

for excelFile in os.listdir('.'):
    if not excelFile.endswith('.xlsx'):
        continue
    print(os.path.split(excelFile))
    wb=openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        sheet=wb[sheetName]
        print(sheet)
    
