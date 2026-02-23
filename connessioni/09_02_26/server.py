from socket import *

#ip_self=  "192.168.2.35"
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)



print("Server ready")
while True:
    try:
        #c_sock,cl_add=serverSocket.accept()
        #print("client: ",cl_add)
        #request = c_sock.recv(1024)
        #request = request.decode('utf-8')
        request="P-test"
        response=""
        f=open("biblioteca.txt", "r+")
        linee=[]
        for pos,line in enumerate(f):
            linee.append(line.split(":"))
        f.close()
        if request[0]=="T":
            for linee_sing in linee:
                if linee_sing[0] ==request[2:]:
                    response="ci sono "+linee_sing[2]+" copie di "+request[2:]+" in libreria"
            if response=="":
                response="titolo non presente"
        #fine richiesta T
        if request[0]=="A":
            for linee_sing in linee:
                if linee_sing[1]==request[2:]:
                    response.append(linee_sing[1]+" ")
            if response=="":
                response="autore non presente"
            else:
                response="autore "+request[2:]+"ha i seguenti libri in libreria "+response
        #fine richiesta A
        if request[0]=="P":
            for linee_sing in linee:
                if linee_sing[0] ==request[2:]:
                    print("A")
            if response=="":
                response="titolo non presente"
            write_list=[]
            for linee_sing in linee:
                write_list.append("-".join(linee_sing))
            print(write_list)
        
        print(response)
        #c_sock.send(response.encode('utf-8'))
    except:
        print("oops something went wrong")
        raise
    #finally:
        #c_sock.close()
    #end finally
#end while