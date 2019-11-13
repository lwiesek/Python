import pygame,sys,random
from pygame.locals import *

pygame.init()
glownyZegar=pygame.time.Clock()

SZEROKOSCOKNA=400
WYSOKOSCOKNA=400
powierzchniaOkna=pygame.display.set_mode((SZEROKOSCOKNA,WYSOKOSCOKNA),0,32)
pygame.display.set_caption('Wykrywanie kolizji')

CZARNY=(0,0,0)
ZIELONY=(0,255,0)
BIALY=(255,255,255)

licznikJedzonek=0
NOWEJEDZONKO=40
ROZMIARJEDZONKA=20
gracz=pygame.Rect(300,100,50,50)
jedzonka=[]
for i in range(20):
    jedzonka.append(pygame.Rect(random.randint(0,SZEROKOSCOKNA-ROZMIARJEDZONKA),
                                random.randint(0,WYSOKOSCOKNA-ROZMIARJEDZONKA),
                                ROZMIARJEDZONKA,ROZMIARJEDZONKA))

ruchLewa=False
ruchPrawa=False
ruchGora=False
ruchDol=False

SZYBKOSCRUCHU=6

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT or event.key==K_a:
                ruchPrawa=False
                ruchLewa=True
            if event.key==K_RIGHT or event.key==K_d:
                ruchLewa=False
                ruchPrawa=True
            if event.key==K_UP or event.key==K_w:
                ruchDol=False
                ruchGora=True
            if event.key==K_DOWN or event.key==K_s:
                ruchGora=False
                ruchDol=True
        if event.type==KEYUP:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==K_LEFT or event.key==K_a:
                ruchLewa=False
            if event.key==K_RIGHT or event.key==K_d:
                ruchPrawa=False
            if event.key==K_UP or event.key==K_w:
                ruchLewa=False
            if event.key==K_DOWN or event.key==K_s:
                ruchLewa=False
            if event.key== K_x:
                gracz.top=random.randint(0,WYSOKOSCOKNA-gracz.height)
                gracz.left=random.randint(0,SZEROKOSCOKNA-gracz.width)
        if event.type==MOUSEBUTTONUP:
            jedzonka.append(pygame.Rect(event.pos[0],event.pos[1],
                                        ROZMIARJEDZONKA,ROZMIARJEDZONKA))

    licznikJedzonek+=1
    if licznikJedzonek>=NOWEJEDZONKO:
        licznikJedzonek=0
        jedzonka.append(pygame.Rect(random.randint(0,SZEROKOSCOKNA-ROZMIARJEDZONKA),
                                    random.randint(0,WYSOKOSCOKNA-ROZMIARJEDZONKA),
                                    ROZMIARJEDZONKA,ROZMIARJEDZONKA))
        powierzchniaOkna.fill(BIALY)

        if ruchDol and gracz.bottom < WYSOKOSCOKNA:
            gracz.top+=SZYBKOSCRUCHU
        if ruchGora and gracz.top > 0:
            gracz.top -=SZYBKOSCRUCHU
        if ruchLewa and gracz.left >0:
            gracz.left-=SZYBKOSCRUCHU
        if ruchPrawa and gracz.right < SZEROKOSCOKNA:
            gracz.right+=SZYBKOSCRUCHU

        pygame.draw.rect(powierzchniaOkna,CZARNY,gracz)

        for jedzonko in jedzonka[:]:
            if gracz.colliderect(jedzonko):
                jedzonka.remove(jedzonko)

        for i in range(len(jedzonka)):
            pygame.draw.rect(powierzchniaOkna,ZIELONY,jedzonka[i])

            pygame.display.update()
            glownyZegar.tick(40)
        
