import threading, time
print('Uruchomienie programu.')
def takeANap():
    time.sleep(5)
    print('Obudz sie!')

threadObj=threading.Thread(target=takeANap)
threadObj.start()

print('Zakonczenie programu.')

