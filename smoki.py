import random
import time

def wyswietlIntro():
    print('''Znajdujesz sie w krainie smokow. Przed soba widzisz dwie jaskinie.
w jednej mieszka przyjazny smok, ktory podzieli sie z toba swoim skarbem. Drugi
smok jest chciwy i glodny, wiec pozre cie bez zmruzenia oka.''')
    print()

def wybierzJaskinie():
    jaskinia=''
    while jaskinia !='1' and jaskinia !='2':
        print('Do ktorej jaskini chcesz wejsc? (1 lub 2)')
        jaskinia=input()

    return jaskinia

def zbadajJaskinie (wybranaJaskinia):
    print('Zblizasz sie do mrocznej jaskini...')
    time.sleep(2)
    print('Wtem! Nagle! Raptem!')
    time.sleep(2)
    print('Pojawia sie straszliwy smok... Otwiera swoja paszcze i...')
    print()
    time.sleep(2)

    przyjaznaJaskinia=random.randint(1,2)

    if wybranaJaskinia==str(przyjaznaJaskinia):
        print('Oddaje ci swoj skarb!')
    else:
        print('Mniam, mniam! Pozera cie w calosci!')

zagrajPonownie='tak'
while zagrajPonownie=='tak' or zagrajPonownie=='t':
    wyswietlIntro()
    numerJaskini=wybierzJaskinie()
    zbadajJaskinie(numerJaskini)

    print('Chcesz zagrac ponownie? (tak lub nie)')
    zagrajPonownie=input()
