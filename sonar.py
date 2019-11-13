import random,sys,math

def utworzNowaPlansze():
    plansza=[]
    for x in range (60):
        plansza.append([])
        for y in range(15):
            if random.randint(0,1)==0:
                plansza[x].append('-')
            else:
                plansza[x].append('`')

    return plansza

def narysujPlansze(plansza):
    wierszCyfryDziesietne=' '
    for i in range(1,6):
        wierszCyfryDziesietne+=(' ' *9)+ str(i)

    print(wierszCyfryDziesietne)
    print(' ' + ('0123456789'*6))
    print()

    for wiersz in range(15):
        if wiersz < 10:
            dodatkowaSpacja=' '
        else:
            dodatkowaSpacja=''
        wierszPlanszy=''
        for kolumna in range(60):
            wierszPlanszy+=plansza[kolumna][wiersz]

        print('%s%s %s %s' (dodatkowaSpacja, wiersz,wierszPlanszy,wiersz))

        print()
        print(' ' +('0123456789'*6))
        print(wierszCyfryDziesietne)

def ukryjLosowoSkrzynie(liczbaSkrzyn):
    skrzynie=[]
    while len(skrzynie) < liczbaSkrzyn:
        nowaSkrzynia=[random.randint(0,59),random.randint(0,14)]
        if nowaSkrzynia not in skrzynie:
            skrzynie.append(nowaSkrzynia)
        return skrzynie

def jestNaPlanszy(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14

def wykonajRuch(plansza,skrzynie,x,y):
    for cx,cy in skrzynie:
        odleglosc=math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
        if odleglosc < najmniejszaOdleglosc:
            najmniejszaOdleglosc=odleglosc

    najmniejszaOdleglosc=round(najmniejszaOdleglosc)

    if najmniejszaOdleglosc==0:
        skrzynie.remove([x,y])
        return 'Znaleziono skrzynie ze skarbami!'
    else:
        if najmniejszaOdleglosc <10:
            plansza[x][y]=str(najmniejszaOdleglosc)
            return 'Skarb wykryty w odleglosci %s od sonara.'
            
