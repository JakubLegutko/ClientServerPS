import socket  
import serial



ser = serial.Serial('COM6',baudrate = 115200, timeout = 1)
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "DISCO-2137"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
def read_sensor_data_and_send():
    for i in range(100) :
         KLO5Data = ser.readline()
         print(KLO5Data)
         msg_length = len(KLO5Data)
         send_length = str(msg_length).encode(FORMAT)
         send_length += b' ' *(HEADER - len(send_length))
         client.send(send_length)
         client.send(KLO5Data)
         print(client.recv(2048).decode(FORMAT))

   



def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
input()
send("Hello World!")
input()
send("Hello World!")
read_sensor_data_and_send()
send(DISCONNECT_MSG)
