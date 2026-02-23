from socket import *

#ip_self=  "192.168.2.35"

serverIP= ""

serverPort=12000

while True:
    Request_Type=input("Inserisci tipo di richiesta (T,A,P) (vuoto x uscire) ").upper()
    if Request_Type=="":
        break
    if Request_Type not in ["T","A","P"]:
        print("Richiesta non valida")
        continue
    Request=Request_Type+"-"+input("Inserisci richiesta: ").upper()
    print("connessione al server...")
    clientSocket=socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverIP,serverPort))
    clientSocket.send(Request.encode('utf-8'))
    print("Richiesta inviata...")
    result=clientSocket.recv(1024)
    result=result.decode('utf-8')
    print("Risposta ricevuta:")
    print(result)
    clientSocket.close()
print("fine")