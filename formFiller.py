#! python3

import pyautogui,time

nameField=(780,338)
submitButton=(749,916)
submitButtonColor=(186,148,130)
submitAnotherLink=(810,232)

formData = [{'name': 'Alicja', 'fear': 'eavesdroppers', 'source': 'wand',
'robocop': 4, 'comments': 'Powiedz Bobowi, że mowie mu czesc.'},
{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
'comments': 'n/a'},
{'name': 'Karol', 'fear': 'puppets', 'source': 'crystal ball',
'robocop': 1, 'comments': 'Prosze zabrac kukielki z pokoju.'},
{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
'robocop': 5, 'comments': 'Chronic niewinnych. Slużyc spoleczenstwu. Stac na strazy prawa.'},
]

pyautogui.PAUSE=0.5

for person in formData:
    print('>>> 5- SEKUNDOWA PRZERWA POZWALAJACA UZYTKOWNIKOWI NACISNAC CTRL-C <<<')
    time.sleep(5)

##    while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
##        time.sleep(0.5)

    print('Wprowadzenie informacji o osobie %s...'% (person['name']))
    pyautogui.click(nameField[0],nameField[1])

    pyautogui.typewrite(person['name'] + '\t')

    pyautogui.typewrite(person['fear'] + '\t')
    
    if person['source'] == 'wand':
        pyautogui.typewrite(['down'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down'])
    pyautogui.press('enter')
    pyautogui.typewrite('\t')

   # Wypełnienie pola RoboCop.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    pyautogui.typewrite(person['comments'])
    time.sleep(1)

    pyautogui.typewrite('\t')
    pyautogui.press('enter')

    print('Kliknieto przycisk Przeslij.')
    time.sleep(5)

    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])
    

    
    

    
