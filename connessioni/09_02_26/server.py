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
        request="A-autore"
        response=""
        f=open("biblioteca.txt", "r")
        lines=[]
        for pos,line in enumerate(f):
            lines.append(line.split(":"))
        f.close()
        if request[0]=="T":
            for lines_sing in lines:
                if lines_sing[0] ==request[2:]:
                    response="ci sono "+lines_sing[2]+" copie di "+request[2:]+" in libreria"
            if response=="":
                response="titolo non presente"
        #fine richiesta T
        if request[0]=="A":
            for lines_sing in lines:
                if lines_sing[1]==request[2:]:
                    response=response+lines_sing[0]+"; "
            response=response.strip("; ")
            if response=="":
                response="autore non presente"
            else:
                response="autore "+request[2:]+" ha i seguenti libri in libreria: "+response
        #fine richiesta A
        if request[0]=="P":
            for lines_sing in lines:
                if lines_sing[0] ==request[2:]:
                    if int(lines_sing[2]>0):
                        lines_sing[2]=str(int(lines_sing[2])-1)
                        response="titolo prenotato. rimangono "+lines_sing[2]+"copie"
                    else:
                        response="titolo presente ma non disponibile"
                    print(lines_sing)
                    print("A")
            if response=="":
                response="titolo non presente"
            write_list=[]
            for lines_sing in lines:
                write_list.append(":".join(lines_sing))
            print(write_list)
            
            f=open("biblioteca.txt", "w")
            #scrivi nuove linee su file
            f.close()
        print(response)
        #c_sock.send(response.encode('utf-8'))
    except:
        print("oops something went wrong")
        raise
    #finally:
        #c_sock.close()
    #end finally
#end while