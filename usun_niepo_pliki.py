import os,shutil

for folderName, subfolders,filenames in os.walk(r'C:\Users\SG0301917\OneDrive - Sabre\Desktop'):
    for filename in filenames:
        if os.path.getsize(folderName +'\\'+ filename) > 104857600:
            #shutil.copy(folderName +'\\'+ filename,r'C:\Users\SG0301917\OneDrive - Sabre\Desktop\ksiazki python\pliki')
            print(folderName +'\\'+ filename + '  rozmiar:  ' + str(os.path.getsize(folderName +'\\'+ filename)))

