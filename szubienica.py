import random
SZUBIENICA_OBRAZKI = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    o   |
        |
        |
       ===''', '''
    
    +---+
    o   |
    |   |
        |
       ===''', '''
    +---+
    o   |
   /|   |
        |
       ===''', '''
    +---+
    o   |
   /|\  |
        |
       ===''', '''
    +---+
    o   |
   /|\  |
   /    |
       ===''', '''
    +---+
    o   |
   /|\  |
   / \  |
       ===''']

slowa = '''baran bocian borsuk bobr foka fretka ges golab indyk
jastrzab jaszczurka jelen kaczka kobra kojot kot koza kret krolik
kruk lama leniwiec lew lis labedz lasica losos los malpa malz
mrowka mul mysz niedzwiedz nietoperz nosorozec orzel osiol owca
pajak panda papuga pawian pies pstrag puma pyton rekin ropucha
skunks sowa szczur traszka tygrys waz wielblad wieloryb wilk wombat
wrona wydra zebra zaba zolw'''.split()

def wylosujSlowo(listaSlow):
    indeksSlowa=random.randint(0,len(listaSlow)-1)
    return listaSlow[indeksSlowa]

def wyswietlPlansze(strzalyNiecelne, strzalyCelne,tajneSlowo):
    print(SZUBIENICA_OBRAZKI[len(strzalyNiecelne)])
    print()

    print('Strzaly niecelne: ',end=' ')
    for litera in strzalyNiecelne:
        print(litera,end=' ')
    print()

    pusteMiejsca='_' * len(tajneSlowo)

    for i in range(len(tajneSlowo)):
        if tajneSlowo[i] in strzalyCelne:
            pusteMiejsca=pusteMiejsca[:i] + tajneSlowo[i] + pusteMiejsca[i+1:]

    for litera in pusteMiejsca:
        print(litera,end=' ')
    print()

def wczytajStrzal(juzPodawane):
    while True:
        print('Podaj litere.')
        strzal = input()
        strzal=strzal.lower()
        if len(strzal)!=1:
            print('Prosze podaj jedna litere!')
        elif strzal in juzPodawane:
            print('Ta litera juz byla. Sprobuj ponownie.')
        elif strzal not in 'abcdefghijklmnopqrstuvwxyz':
            print('Prosze podac litere!')
        else:
            return strzal

def zagrajPonownie():
    print('Chcesz zagrac ponownie? (tak lub nie)')
    return input().lower().startswith('t')

print('S Z U B I E N I C A')
strzalyNiecelne= ''
strzalyCelne=''
tajneSlowo=wylosujSlowo(slowa)
koniecGry=False

while True:
    wyswietlPlansze(strzalyNiecelne,strzalyCelne, tajneSlowo)

    strzal=wczytajStrzal(strzalyNiecelne + strzalyCelne)

    if strzal in tajneSlowo:
        strzalyCelne = strzalyCelne + strzal

        wszystkieLiteryOdgadniete=True
        for i in range(len(tajneSlowo)):
            if tajneSlowo[i] not in strzalyCelne:
                wszystkieLiteryOdgadniete=False
                break
        if wszystkieLiteryOdgadniete:
            print('Tak! Tajne slowo to "' + tajneSlowo + '" !Zwyciestwo!')
            koniecGry=True
    else:
        strzalyNiecelne=strzalyNiecelne+strzal

        if len(strzalyNiecelne)==len(SZUBIENICA_OBRAZKI)-1:
            wyswietlPlansze(strzalyNiecelne,strzalyCelne,tajneSlowo)
            print('Nie masz juz wiecej strzalow! \nPo ' + str(len(strzalyNiecelne)) + ' strzalach niecelnych i ' +
                  str(len(strzalyCelne))+ ' strzalach celnych, tajne slowo to "' + tajneSlowo + '"')
            
                  
            koniecGry=True

    if koniecGry:
         if zagrajPonownie():
             strzalyNiecelne=''
             strzalyCelne=''
             koniecGry=False
             tajneSlowo=wylosujSlowo(slowa)
         else:
             break
