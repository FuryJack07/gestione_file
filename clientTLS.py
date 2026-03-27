import socket
import ssl

HOST = "192.168.1.1"  
PORT = 65432


context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  


context.load_cert_chain(certfile="client.crt", keyfile="client.key") 
context.load_verify_locations("ca.crt")  
context.verify_mode = ssl.CERT_REQUIRED  


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    with context.wrap_socket(sock, server_hostname=HOST) as secure_sock:
        print("Connessione sicura stabilita con il server.")
        
      
        secure_sock.sendall(b"Ciao sono il client")
        
        
        server_msg = secure_sock.recv(1024).decode()
        print(f"Messaggio ricevuto dal server: {server_msg}")
