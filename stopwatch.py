#! python3
import time

print('Nacisnij Enter, aby rozpoczac. Kolejne nacisniecie Enter oznacza nowe okrazenie.')
input()
print('Rozpoczeto dzialanie.')
startTime=time.time()
lastTime=startTime
lapNum=1

try:
    while True:
        input()
        lapTime=round(time.time()-lastTime,2)
        totalTime=round(time.time()-startTime,2)
        print('Okrazenie #%s: %s (%s)' %(lapNum,totalTime,lapTime),end='')
        lapNum+=1
        lastTime=time.time()
except KeyboardInterrupt:
    print('\nGotowe!')
              
