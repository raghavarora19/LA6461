import socket
host = "www.ptsv2.com"
port = 80

headers = """\
POST /t/raghav/post HTTP/1.1\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 29\r
Host: ptsv2.com\r
Connection: close\r
\r\n """

body = 'username=raghav&password=pass'
body_bytes = body.encode('ascii')
header_bytes = headers.format(
    content_type="application/x-www-form-urlencoded",
    content_length=len(body_bytes),
    host=str(host) + ":" + str(port)
).encode('iso-8859-1')

payload = header_bytes + body_bytes
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.ptsv2.com", 80))
s.sendall(payload)
payload = s.recv(1024)
print('Result : \n', payload.decode())
s.close()