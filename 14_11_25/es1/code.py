numeri = open('numeri.txt','r')
pari = open('pari.txt','w')
dispari = open('dispari.txt','w')

for n in numeri:
    if (int(n)%2==0):
        pari.write(n)
    else:
        dispari.write(n)

numeri.close()
pari.close()
dispari.close()