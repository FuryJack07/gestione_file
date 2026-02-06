from socket import *

f=open("file.txt", "r")

#ip_self=  "192.168.2.35"
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("Server ready")
while True:
    try:
        n_line=int(input("inserisci numero di linee"))
    except:
        print("numero non valido")
        continue
    for i in range(n_line):
        print(f.readline())
    #eof/0 check to end