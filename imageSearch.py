#! python3
import os
from PIL import Image

ext=('.jpg','.png','.JPG','.PNG')
numPhotoFiles=0
numNonPhotoFiles=0
try:
    for foldername,subfolders,filenames in os.walk('C:\\'):
        
        for filename in filenames:
            if not filename.endswith(ext):
                numNonPhotoFiles+=1
                continue

            im=Image.open(filename)
            width,height=im.size
            if ((width >50) and (height > 50)):
                numPhotoFiles+=1
                print(os.path.abspath(filename))
            else:
                numNonPhotoFiles+=1
                print(os.path.abspath(filename))
except:
    pass


print(numPhotoFiles)
print(numNonPhotoFiles)
            
            
