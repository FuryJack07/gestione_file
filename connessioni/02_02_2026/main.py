from socket import *

#ip_self=  "192.168.2.35"
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print("Server ready")
while True:
    try:
        c_sock,cl_add=serverSocket.accept()
        print("client: ",cl_add)
        data = c_sock.recv(1024)
        data = data.decode('utf-8')
        print("from: ",data)
        data = data.upper()
        print("to: ",data)
        data = data.encode('utf-8')
        c_sock.send(data)
    except:
        print("oops something went wrong")
    finally:
        c_sock.close()
    #end finally
#end while