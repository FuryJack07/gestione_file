val = open("valutazioni.txt","r")

valutazioni=[]

for pos,line in enumerate(val):
    valutazioni.append(line.split(":"))
val.close()


lista=[]

somma=0
media=0
valori=0
while True:
    lista=[]
    for val_sing in valutazioni:
        if val_sing[1] not in lista:
            lista.append(val_sing[1])
    print(lista)
    somma=0
    media=0
    valori=0
    materia=input("Inserisci una materia (invio per finire): ").strip("\n")
    if (materia==""):
        break
    lista=[]
    for val_sing in valutazioni:
        if val_sing[0] not in lista:
            lista.append(val_sing[0])
    print(lista)
    alunno=input("Inserisci un alunno (invio per la media generale della materia): ")
    if (alunno==""):
        #media generale materia
        for val_sing in valutazioni:
            if (val_sing[1]==materia):
                somma=somma+float(val_sing[2])
                valori=valori+1
            #end if
        #end for
    #end if
    else:
        for val_sing in valutazioni:
            if (val_sing[1]==materia):
                if(val_sing[0]==alunno):
                    somma=somma+float(val_sing[2])
                    valori=valori+1
                #end if
            #end if
        #end for
    #end else
    if (valori==0):
        print("nessuna valutazione")
    else:
        media=round(somma/valori,2)
        print(media)
#end while