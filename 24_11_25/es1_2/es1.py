file = open("file.txt","a")

def wr(fil,i,eol=False):
    fil.write(i)
    fil.write(";")
    if eol:
        fil.write("\n")

while True:
    inp=input("inserisci città (invio per fine): ")
    if inp=="":
        break
    wr(file,inp)
    while True:
        inp=input("inserisci temperatura °c (numero float): ")
        try:
            float(inp)
            break
        except:
            print("inserisci un numero")
    wr(file,inp)
    while True:
        inp=input("inserisci umidità (numero float): ")
        try:
            float(inp)
            break
        except:
            print("inserisci un numero")
    wr(file,inp,True)
file.close()