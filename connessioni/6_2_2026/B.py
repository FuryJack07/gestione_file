from socket import *

#ip_self=  "192.168.2.35"
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("B ready")
while True:
    data,cl_add=serverSocket.recvfrom(1024)
    print("client: ",cl_add)
    data = data.decode('utf-8')
    print(data)
#end while
serverSocket.close()