import socket  
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'ascii'
DISCONNECT_MSG = "DISCO-PLS"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
#bound socket to machine address

def handle_client(conn, addr):
    print("[NEW CONN!]")
    print(addr)
    print ("Connected!")
    connected = True
    while connected :
       try:
        msg_length = conn.recv(HEADER).decode(FORMAT,"ignore")
       except ConnectionResetError :
           connected = False
           print("OOPS! Connection failed suddenly!")
           break
       except ConnectionAbortedError:
                        connected =False
                        print("OOPS! someone triggered Ctrl+C on client side!")
                        break
       if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT,"ignore")
           

            if msg == DISCONNECT_MSG:
                connected = False
                
                try:
                    
                    conn.send("Disconnecting on client request".encode(FORMAT,"ignore"))
                except ConnectionAbortedError:
                        connected =False
                        print("OOPS! someone triggered Ctrl+C on client side!")
                        break
       print(addr,msg)
       address = ''.join(str(addr)) 
       with open(address+'.txt', 'a') as address:
            print(msg, file=address)
       conn.send("Message Recieved boii".encode(FORMAT,"ignore"))
        
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
