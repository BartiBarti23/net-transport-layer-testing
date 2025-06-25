from socket import socket, AF_INET, SOCK_DGRAM
import json

with open("config.json") as f:
    config = json.load(f)

VM_IP = config.get("VM_IP", "127.0.0.1")  # default to localhost if not set
print(f"Using VM IP: {VM_IP}")

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server is ready to receive messages")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
