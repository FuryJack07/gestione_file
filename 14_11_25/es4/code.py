val = open("valutazioni.txt","r")

valutazioni=[]

for pos,line in enumerate(val):
    print(pos)
    print(line)
    
    valutazioni.append(line.split(":"))
    
val.close()

print(valutazioni)
print(valutazioni[0])
print(valutazioni[0][0])