import socket  
import serial
import time
import sys



PORTS = ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8']
while True:
       try:
        COM = sys.argv[1]
        if COM in PORTS :
            break
        else :
            print("Usage: client.py COM| where | is COM port number!")
            sys.exit()
       except IndexError :
            print("Usage: client.py COM| where | is COM port number!")
            sys.exit()
            

while True:
   try:
     ser = serial.Serial(COM,baudrate = 9600, timeout = 1)
     break
   except serial.serialutil.SerialException:
       device = False
       for i in range(10): 
         print(f"Connect device! Attempt number {i+1}")
         time.sleep(2)
         try:
            ser = serial.Serial(COM,baudrate = 9600, timeout = 1)
            device = True
            break
         except serial.serialutil.SerialException:
             print("...")
   if(device == False):
            print("No response from device, exiting...")
            sys.exit()
   else:
            break
HEADER = 64
PORT = 5050
FORMAT = 'ascii'
DISCONNECT_MSG = "DISCO-PLS"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        client.connect(ADDR)
        break
    except ConnectionRefusedError:
        ConnectionRestored = False
        for i in range(5):
           
            print(f"Server is unreachable, retrying... attempt number {i+1} ")
            time.sleep(3)
            try:
                client.connect(ADDR)
                print("Connected!")
                ConnectionRestored = True
                break
            except ConnectionRefusedError:
                print("...")
        if(ConnectionRestored == False):
            print("No response from server, exiting...")
            sys.exit()
        else:
            break
def read_sensor_data_and_send():
    for i in range(100) :
         KLO5Data = ser.readline()
         print(KLO5Data)
         msg_length = len(KLO5Data)
         send_length = str(msg_length).encode(FORMAT)
         send_length += b' ' *(HEADER - len(send_length))
         try:
            client.send(send_length)
         except ConnectionResetError:
             print("OOPS! Server stopped responding and died.Client will exit as it has no target to send to")
             sys.exit()
         client.send(KLO5Data)
         print(client.recv(2048).decode(FORMAT))

   



def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER - len(send_length))
    try:
        client.send(send_length)
    except ConnectionResetError:
        print("OOPS! Server stopped responding and died.Client will exit as it has no target to send to")
        sys.exit()
    try:
        client.send(message)
    except ConnectionResetError:
        print("OOPS! Server stopped responding and died.Client will exit as it has no target to send to")
        sys.exit()
    print(client.recv(2048).decode(FORMAT))


#send("Hello World!")
input()
#send("Hello World!")
input()
#send("Hello World!")

read_sensor_data_and_send()
send(DISCONNECT_MSG)
