import json

dati={}

while True:
    NoCo=input('Inserisci "nome cognome" (vuoto per fine) ')
    if NoCo=="":
        break
    if NoCo in dati:
        print('"Nome cognome" già inserito. riprovare')
        continue
    Squa=input('Inserisci "squadra" ')
    while True:
        try:
            Goal=int(input('Inserisci "goal" (int) '))
            break
        except ValueError:
            print("int non valido")
    dati[NoCo]=[Squa,Goal]
print(dati)
with open("test.json","w") as f:
    json.dump(dati,f)