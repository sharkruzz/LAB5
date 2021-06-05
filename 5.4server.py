import socket

s = socket.socket()
host = '192.168.56.105'
port = 8080
s.bind((host,port))
s.listen(1)
print (host)
print ("waiting for connection..")
conn,addr = s.accept()
print (addr, "has connected")

filename = input(str("please enter the filenameof the file : "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print ("Data has been trasmitted successfully")
