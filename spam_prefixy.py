import os,shutil,re

regexy=re.compile(r'(spam)([0-9]{3})(.txt)')
for folderName, subfolders,filenames in os.walk(r'C:\Users\SG0301917\OneDrive - Sabre\Desktop\ksiazki python\pliki\tekstowe'):
    for filename in filenames:
        mo=regexy.search(filename)
        print(mo.group(2))
