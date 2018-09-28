import socket
host = "www.facebook.com"
port = 80

headers = """\
POST /auth HTTP/1.1\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 29\r
Host: www.facebook.com\r
Connection: close\r
\r\n """

body = 'userName=Sonali&password=pass'
body_bytes = body.encode('ascii')
header_bytes = headers.format(
    content_type="application/x-www-form-urlencoded",
    content_length=len(body_bytes),
    host=str(host) + ":" + str(port)
).encode('iso-8859-1')

payload = header_bytes + body_bytes
