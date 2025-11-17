testo = open("testo.txt","r")
perc = open("perc.txt","w")


char=' '

caratteri_all=0
caratteri_seek={}

char= testo.read(1)

while (char!=''):
    caratteri_all=caratteri_all+1
    if char in caratteri_seek:
        caratteri_seek[char] += 1
    else:
        caratteri_seek[char] = 1
    char= testo.read(1)

print(caratteri_all)
print(caratteri_seek)

for c in caratteri_seek:
    perc.write(c)
    perc.write(" = ")
    perc.write(str(round(caratteri_seek[c]/caratteri_all*100,2)))
    perc.write("%")
    perc.write("\n")
    
testo.close()
perc.close()