import re
import os
##
##file=open("madlibs.txt")
##s=file.read()
##file.close()
##

regexy=re.compile(input("Podaj wyrazenie regularne: ").upper())
##
##
##for i in regexy.findall(s):
##    inputy=input('Podaj zamiennk za %s: ' %i)
##    s=regexy.sub(inputy,s,1)
##
##print(s)
##
##file=open('madlibs_ans','w')
##file.write(s)
##file.close()

znal=[]
path="C:\\Users\\SG0301917\\OneDrive - Sabre\\Desktop\\ksiazki python\\"
all_files=os.listdir(path)
for file in all_files:
    if file[-3:]=="txt":
        otw=open(file)
        s=otw.read()
        otw.close()
        znal=znal + regexy.findall(s)
print(znal)
    
