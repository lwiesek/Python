#! python3
#removeCsvHeader.py
#znajdujacych sie w biezacym katalogu roboczym

import csv,os

os.makedirs('headerRemoved',exist_ok=True)

for csvFilename in os.listdir('removeCsvHeader\\'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Usuwanie naglowka z pliku ' + csvFilename + '...')
    csvRows=[]
    csvFileObj=open('removeCsvHeader\\' + csvFilename)
    readerObj=csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num==1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    #zapis pliku csv
    
    csvFileObj=open(os.path.join('headerRemoved',csvFilename),'w',
                    newline='')
    csvWriter=csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
