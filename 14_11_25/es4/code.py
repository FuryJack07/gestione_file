val = open("valutazioni.txt","r")

valutazioni=[]

for pos,line in enumerate(val):
    print(pos)
    print(line)
    
    valutazioni[pos]=line.split(":")
    #Traceback (most recent call last):
        #File "/home/pi/gestione_file/14_11_25/es4/code.py", line 9, in <module>
            #valutazioni[pos].append(line.split(":"))
    #IndexError: list index out of range
    
    
val.close()

print(valutazioni)