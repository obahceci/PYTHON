import socket 

PORT=5050
SERVER="192.168.0.30"

HEADER=64
FORMAT="utf-8"
DISCONNECT_MESSAGE="exit"
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ADDR))

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER-len(send_length))   #64bytelık veri göndermek için 64bytetan mesajın uzunluğun çıkarıp o kadar boşluk eklemek
    
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT)) 


send("Hello World")

send("Hello Everyone")

send("Hello Ali")

send(DISCONNECT_MESSAGE)