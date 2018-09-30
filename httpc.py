
import socket

request = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.com", 80))
s.sendall(request.encode())
result = s.recv(1024)
abc = result.decode()
body=abc.split('\r\n\r\n')
#print('Result : \n', result.decode())
print('Result 2: \n ', body[0])
s.close()