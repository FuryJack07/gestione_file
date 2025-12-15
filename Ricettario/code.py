import json

try:
    with open("ricettario.json","r") as f:
        ricette=json.load(f)
except FileNotFoundError:
    print("Nessun ricettario trovato. creazione ricettario vuoto...")
    ricette={}
except:
    print("errore sconosciuto. creazione ricettario vuoto...")
    ricette={}



while True:
    nome=input("Inserire nome ricetta: ")
    if nome=='':
        break
    while True:
        ingrediente=input("inserire nome ingrediente: ")
        if ingrediente=='':
            print("nome ingrediente vuoto. riprovare")
            continue
        break
    while True:
        try:
            quantita=float(input("inserire quantità ingrediente: "))
            break
        except:
            print("valore float non valido. riprovare")
        #endwhile
    if nome in ricette:
        ricette[nome][ingrediente]=quantita
    else:
        ricette[nome]={ingrediente:quantita}
    with open("ricettario.json","w") as f:
        json.dump(ricette,f)
        print(ricette[nome])
print("Scrittura ricettario completata: ")
print(ricette)


print("Fase di lettura: ")

while True:
    nome=input("Inserire nome ricetta: ")
    if nome=='':
        break
    if (nome not in ricette):
        print("Ricetta non esistente. riprovare")
        continue
    for ing in ricette[nome]:
        print(ing, end="= ")
        print(ricette[nome][ing])
print("fine")