from socket import *

#ip_self=  "192.168.2.35"
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("Server ready")
while True:
#    try:
    data,cl_add=serverSocket.recvfrom(1024)
    print("client: ",cl_add)
    data = data.decode('utf-8')
    print("from: ",data)
    data = data.upper()
    print("to: ",data)
    data = data.encode('utf-8')
    serverSocket.sendto(data,cl_add)
#    except:
#        print("oops something went wrong")
    #finally:
serverSocket.close()
    #end finally
#end while
