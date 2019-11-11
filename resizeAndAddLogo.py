import os
from PIL import Image

SQUARE_FIT_SIZE=300
LOGO_FILENAME='catlogo.png'

logoIm=Image.open(LOGO_FILENAME)
logoIm=logoIm.resize((50,50))
logoIm.save('catlogo.png')
logoWidth,logoHeight=logoIm.size

os.makedirs('withLogo',exist_ok=True)
ext=['.jpg','.png','.gif','.bmp']
extL=tuple(ext)
extU=[]
for i in range(len(ext)):
    extU.append(ext[i].upper())
    
ext=extL+tuple(extU)    
    

for filename in os.listdir('.'):
    if not(filename.endswith(ext)) \
       or filename ==LOGO_FILENAME:
        continue

    im=Image.open(filename)
    width,height=im.size

    if width >SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height=int((SQUARE_FIT_SIZE/width)*height)
            width=SQUARE_FIT_SIZE
        else:
            width=int((SQUARE_FIT_SIZE/height)*width)
            height=SQUARE_FIT_SIZE

        print('Zmiana wielkosci obrazu %s...' % (filename))
        im=im.resize((width,height))

        print('Dodanie logo do obrazu %s...' % (filename))
        im.paste(logoIm,(width - logoWidth,height-logoHeight), logoIm)

        im.save(os.path.join('withLogo',filename))
        
