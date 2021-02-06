# Cli-Chat
A Command Line Chat App made with Python 
<br>
This can also be used as an example for Socket programming

## Dependencies
- Socket
- Sys
- Threading

## General Instructions
  ### Server
    python server.py
  ### Client
    python server.py {Address of the server}
    i.e- python server.py 127.0.0.1
    
## How it works
  ### Server
     The server socket initializes and binds with the address and port
     It constantly listens for incoming connections
     A "handler" thread starts for each incoming connections
     The thread looks for the message from their respective clients and sends it to the other clients 
     
  ### Client
     The client socket is initialized
     The sendMsg daemon is initialized 
     It send the message in form of bytes to the server which further sends it to other clients
     The recvMsg daemon is initialized 
     It recieves message from the server which is initially sent by some other client
 
 #### This is the whole process which takes place which causes the CLI Chat app to work
 #### Read the code to understand the process in a better manner
