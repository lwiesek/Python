import time
def calcProd():
    product=1
    for i in range(1,100000):
        product=product*i
    return product

starttime=time.time()
prod=calcProd()
endtime=time.time()

print('Wynik sklada sie z %s cyfr.' %(len(str(prod))))
print('Wykonanie kodu zabralo %s sekund.' %(endtime-starttime))
