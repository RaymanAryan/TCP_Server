#Importing in-built module
from array import *
from socket import *
cli = socket()
#Connecting to the server
cli.connect(("127.0.0.1",9577))
#receiving the order and then display it.
print(cli.recv(1024).decode())

 #Preparing the data
N = input("Name")+ ",\n"
A = input("Address")+",\n"
S = input("School")+'.\n'
St = input("Story")+'\n'
Data = list([N,A,S,St])
    #Sending data
for i in Data :
        cli.send(bytes(i,'utf-8'))
#TO SHOW THE PROCESS IS COMPLETED
print("Data is Send.")
print("Bye")



