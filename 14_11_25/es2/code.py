testo = open("testo.txt","r")

char=' '

carattere = input("inserisci carattere: ")

caratteri_all=0
caratteri_seek=0

char= testo.read(1)

while (char!=''):
    caratteri_all=caratteri_all+1
    if (char==carattere):
        caratteri_seek=caratteri_seek+1
    char= testo.read(1)

print(caratteri_all)
print(caratteri_seek)
print(round((caratteri_seek/caratteri_all*100), 2) , end='%')