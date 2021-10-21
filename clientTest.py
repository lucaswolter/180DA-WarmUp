import socket

client = socket.socket(socket.AF_INET, socet.SOCK_STREAM)
host = socket.gethostname()
host_ip = '131.179.60.147'
port = 8080
client.connect((host_ip, 8080)_
client.send('I am CLIENT'.encode())
from_server = client.recv(4096)
client.close()
print(from_server.decode('ascii'))
