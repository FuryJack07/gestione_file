with open("Messaggio.txt","r") as m:
    messaggio=m.read()



while True:
    try:
        key=int(input("Inserisci chiave (5-80): "))
        if (key<5)|(key>80):
            raise OverflowError
        break
    except OverflowError:
        print("chiave fuori range")
    except ValueError:
        print("err: numero non valido")
    except KeyboardInterrupt:
        raise
    except:
        print("what did you do????????????")
with open("Criptico.txt","w") as C:
    for c in messaggio:
        if ord(c) in range(32,123):
            char_id=ord(c)
            char_id_new=char_id+key
            if char_id_new>=123:
                char_id_new=char_id_new-123+32
            C.write(chr(char_id_new))
        else:
            C.write(c)
print("done")