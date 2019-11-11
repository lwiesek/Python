import random

print('Czesc! Jak masz na imie?')
mojeImie=input()

liczba=random.randint(1,20)
print('Sluchaj, ' + mojeImie + ' , mysle o liczbie z przedzialu 1 do 20.')

for wykonaneProby in range(6):
    print('Sprobuj odgadnac.')
    probaOdgadniecia=input()
    probaOdgadniecia=int(probaOdgadniecia)

    if probaOdgadniecia < liczba:
        print('Twoja liczba jest za mala')

    if probaOdgadniecia > liczba:
        print('Twoja liczba jest za duza')

    if probaOdgadniecia == liczba:
        break

if probaOdgadniecia == liczba:
    wykonaneProby=str(wykonaneProby +1)
    print('Swietna robota, ' +mojeImie + '! Udalo ci sie odgadnac w ' + wykonaneProby + ' probach!')

if probaOdgadniecia !=liczba:
    liczba=str(liczba)
    print('Niestety nie. Liczba, ktora mialem na mysli to ' + liczba + '.')
