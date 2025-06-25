from socket import socket, AF_INET, SOCK_STREAM
import json

with open("config.json") as f:
    config = json.load(f)

VM_IP = config.get("VM_IP", "127.0.0.1")  # default to localhost if not set
print(f"Using VM IP: {VM_IP}")

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready to receive messages")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()