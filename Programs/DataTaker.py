#Importing in-built module
from socket import *
#Making a socket for the server
ver = socket()
#bind the ip address of the hardware's network and port
ver.bind(("127.0.0.1",9577))
#Number of client that can be handle at a Time
ver.listen(1)
print("Waiting for Client")
try:
        while True:#when it accept a client the while block will be activate
                # accepting the client
                clo, asd = ver.accept()
                clo.send(bytes("Please provide us your data...", "utf-8"))
                print("Connect to a client",asd)#asd is the ip addess and the port number of the client
                #print the story then details on the file
                for i in range(3) :
                        f = open('filedatabase', 'a')
                        Data = (clo.recv(100).decode())
                        f.write(Data)
                        f.close
                        if i == 3:
                                print("Data for A client is Taken!")

finally:
   #closes the client
   clo.close()


