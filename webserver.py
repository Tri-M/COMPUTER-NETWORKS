
from socket import *

def main():
  PORT = 8080
  serverSocket = socket(AF_INET,SOCK_STREAM)
  serverSocket.bind(('',PORT))
  serverSocket.listen(5)
  print ("Serving HTTP services on port number %s" %PORT)
  
  while True:
    print ('Ready to serve...')
    clientSocket, addr = serverSocket.accept()
    
    try:
      message = clientSocket.recv(2048)
      filename = message.split()[1]
      print ('The requested file is:', filename[1:], '\n')
      f = open(filename[1:])
      outputData = f.read()
      print (outputData)
      
      clientSocket.send('\nHTTP/1.1 200 OK\n\n') 
      
      clientSocket.send(outputData)
      clientSocket.close()
      
    except IOError:
      print ("404 not found")
      clientSocket.send("\nHTTP/1.1 404 NOT FOUND ERROR \nThe requested URL was not found on the server!")
      #Error message for file not found
      clientSocket.close()
      pass
    
    break
    serverSocket.close()
  pass
if __name__=='__main__':
    main()