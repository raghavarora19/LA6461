
import socket

request = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.com", 80))
s.sendall(request.encode())
result = s.recv(1024)
print('Result : \n', result.decode())
s.close()