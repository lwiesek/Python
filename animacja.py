import pygame,sys,time
from pygame.locals import *

pygame.init()

SZEROKOSCOKNA=400
WYSOKOSCOKNA=400
powierzchniaOkna=pygame.display.set_mode((SZEROKOSCOKNA,WYSOKOSCOKNA),0,32)
pygame.display.set_caption('Animacja')

LEWADOL='lewaDol'
PRAWADOL='prawaDol'
LEWAGORA='lewaGora'
PRAWAGORA='prawaGora'

SZYBKOSCRUCHU=4

BIALY=(255,255,255)
CZERWONY=(255,0,0)
ZIELONY=(0,255,0)
NIEBIESKI=(0,0,255)

r1= {'rect':pygame.Rect(300,80,50,100),'kolor':CZERWONY,'kier':PRAWAGORA}
r2= {'rect':pygame.Rect(200,200,20,20),'kolor':ZIELONY,'kier':LEWAGORA}
r3= {'rect':pygame.Rect(100,150,60,60),'kolor':NIEBIESKI,'kier':LEWADOL}

ramki=[r1,r2,r3]

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    powierzchniaOkna.fill(BIALY)

    for r in ramki:
        if r['kier']==LEWADOL:
            r['rect'].left-=SZYBKOSCRUCHU
            r['rect'].top+=SZYBKOSCRUCHU
        if r['kier']==PRAWADOL:
            r['rect'].left+=SZYBKOSCRUCHU
            r['rect'].top+=SZYBKOSCRUCHU
        if r['kier']==LEWAGORA:
            r['rect'].left-=SZYBKOSCRUCHU
            r['rect'].top-=SZYBKOSCRUCHU
        if r['kier']==PRAWAGORA:
            r['rect'].left+=SZYBKOSCRUCHU
            r['rect'].top-=SZYBKOSCRUCHU

        if r['rect'].top < 0:
            if r['kier']==LEWAGORA:
                r['kier']=LEWADOL
            if r['kier']==PRAWAGORA:
                r['kier']=PRAWADOL

        if r['rect'].bottom > WYSOKOSCOKNA:
            if r['kier']==LEWADOL:
                r['kier']=LEWAGORA
            if r['kier']==PRAWADOL:
                r['kier']=PRAWAGORA

        if r['rect'].left < 0:
            if r['kier']==LEWADOL:
                r['kier']=PRAWADOL
            if r['kier']==LEWAGORA:
                r['kier']=PRAWAGORA

        if r['rect'].left > SZEROKOSCOKNA:
            if r['kier']==PRAWADOL:
                r['kier']=LEWADOL
            if r['kier']==PRAWAGORA:
                r['kier']=LEWAGORA

        pygame.draw.rect(powierzchniaOkna,r['kolor'],r['rect'])

    pygame.display.update()
    time.sleep(0.02)
    
        

        
            
            
            
