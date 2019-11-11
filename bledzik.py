import random
liczba1=random.randint(1,10)
liczba2=random.randint(1,10)
print('Ile to jest ' + str(liczba1) + ' + ' + str(liczba2) + '?')
odpowiedz=input()
if odpowiedz ==liczba1 + liczba2:
    print('Zgadza sie!')
else:
    print('Zle! prawidlowa odpowiedz to ' + str(liczba1 + liczba2))
