import socket
UDP_IP = "192.168.56.105"
UDP_PORT = 8080
MESSAGE = 'soket sedang menunggu client!'
print("IP: %s" % UDP_IP)
print("PORT: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("berjaya buat sokett")

sock.bind((UDP_IP, UDP_PORT))
print("berjaya bind soket di port: %s" % UDP_PORT)

print("%s" % MESSAGE)

while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
