from socket import socket, AF_INET, SOCK_STREAM
import json

with open("config.json") as f:
    config = json.load(f)

VM_IP = config.get("VM_IP", "127.0.0.1")  # default to localhost if not set
print(f"Using VM IP: {VM_IP}")

serverName = VM_IP
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))  # Negotiating process
sentence = input("Lowercase input sentence: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From server: ", modifiedSentence.decode())
clientSocket.close()