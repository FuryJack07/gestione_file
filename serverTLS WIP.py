import socket
import ssl
HOST = "192.168.1.127"
PORT=65432

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
