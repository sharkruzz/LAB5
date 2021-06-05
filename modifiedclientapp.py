import socket

UDP_IP = "192.168.56.105"
UDP_PORT = 8080
MESSAGE = "hi, saya client. Terima Kasih!"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect((UDP_IP,UDP_PORT))
data = sock.recv(1024)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print(data)
sock.close()
