#import socket module
from socket import *
import sys # In order to terminate the program

WORING_DIRECTORY = "/home/pipr/Pulpit/Web-server-lab-Kurose"
SERVER_ADDR = "server.html"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        filename = WORING_DIRECTORY + filename
        outputdata = ""
        with open(filename, "r") as f:
            outputdata = f.read()
        
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        
        
        #Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()
    except IOError as e:
        print("Error opening file:", e)
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data 