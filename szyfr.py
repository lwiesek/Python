SYMBOLE='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_ROZMIAR_KLUCZA=len(SYMBOLE)

def ustawTryb():
    while True:
        print('Chcesz szyfrowac czy deszyfrowac czy silowo odszyfrowac komunikat?')
        tryb=input().lower()
        if tryb in ['szyfrowanie','s','deszyfrowanie','d','technika silowa','t']:
            return tryb
        else:
            print('Wpisz "szyfrowanie" lub "s" lub "deszyfrowanie" lub "d" lub "technika silowa" lub "t".')

def wczytajKomunikat():
    print('Wpisz swoj komunikat:')
    return input()

def wczytajKlucz():
    klucz=0
    while True:
        print('Podaj liczbowy klucz (1-%s)' % (MAX_ROZMIAR_KLUCZA))
        klucz=int(input())
        if (klucz >=1 and klucz <=MAX_ROZMIAR_KLUCZA):
            return klucz

def przeksztalcKomunikat(tryb,komunikat,klucz):
    if tryb[0] == 'd':
        klucz= -klucz
    poPrzeksztalceniu= ''

    for symbol in komunikat:
        indeksSymbolu=SYMBOLE.find(symbol)
        if indeksSymbolu== -1:
            poPrzeksztalceniu+= symbol
        else:
            indeksSymbolu+=klucz

            if indeksSymbolu >=len(SYMBOLE):
                indeksSymbolu -=len(SYMBOLE)
            elif indeksSymbolu < 0:
                indeksSymbolu+=len(SYMBOLE)

            poPrzeksztalceniu +=SYMBOLE[indeksSymbolu]
    return poPrzeksztalceniu

tryb=ustawTryb()
komunikat=wczytajKomunikat()
if tryb[0] != 't':
    klucz=wczytajKlucz()
print('Twoj komunikat po przeksztalceniu brzmi:')
if tryb[0]!='t':
    print(przeksztalcKomunikat(tryb,komunikat,klucz))
else:
    for klucz in range(1,MAX_ROZMIAR_KLUCZA + 1):
        print(klucz, przeksztalcKomunikat('deszyfrowanie',komunikat,klucz))

