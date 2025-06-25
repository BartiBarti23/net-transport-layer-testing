from socket import socket, AF_INET, SOCK_DGRAM
import json

with open("config.json") as f:
    config = json.load(f)

VM_IP = config.get("VM_IP", "127.0.0.1")  # default to localhost if not set
print(f"Using VM IP: {VM_IP}")

serverName = VM_IP
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Zdanie wejściowe zapisane małymi literami: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()