val = open("file.txt","r")

valori=[]

for pos,line in enumerate(val):
    valori.append(line.split(";"))
val.close()

lista=[]
for val_sing in valori:
    if val_sing[0] not in lista:
        lista.append(val_sing[0])
print(lista)
print(valori)
somma=0
media=0
valo=0

citta=input("Inserisci una città: ").strip("\n")

print(valori)

#fare media