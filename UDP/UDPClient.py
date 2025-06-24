from socket import socket, AF_INET, SOCK_DGRAM
serverName = '192.168.1.247'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Zdanie wejściowe zapisane małymi literami: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()