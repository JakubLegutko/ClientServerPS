import socket  
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "DISCO-2137"
# got AF_INET socket now :D
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
#bound socket to machine address

def handle_client(conn, addr):
    print("[NEW CONN!]")
    print(addr)
    print ("Connected!")
    connected = True
    while connected :
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
        print(addr,msg)
    conn.close()

def start():
    server.listen()
    print(f"[LISTEN] Server is listening on {SERVER}")
    while True:
       conn, addr = server.accept()
       thread = threading.Thread(target=handle_client, args=(conn,addr))
       thread.start()
       print("[ACTIVE CONNS] :")
       print(threading.activeCount() -1)

print("[STARTING]")
start()
