a = """HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Fri, 05 Oct 2018 07:55:30 GMT
Content-Type: text/html
Content-Length: 178
Connection: close
Location: http://www.concordia.com/get
"""

b="""HTTP/1.1 302 Found
Date: Fri, 05 Oct 2018 04:54:18 GMT
Server: Server
Location: http://www.amazon.com
Content-Length: 205
Connection: close
Content-Type: text/html; charset=iso-8859-1"""

c="""HTTP/1.0 302 Found
Location: http://www.ieee.org/
Server: BigIP
Connection: close
Content-Length: 0
"""


   # get(verbose, header, optional, Location)

#print (c.find('Location:'))
if a.find('Location:'):
    split=a.splitlines()
    print(split)
    res = [i for i in split if 'Location:' in i]
    print(res)
    reurl=res[0].split(': ')
    result=reurl[1].split('//')
    print(result)
    finalreurl = [i for i in result if '' in i]
    print(finalreurl)
    #get(verbose, header, optional, Location)





#if
 #//import socket
#URL= 'www.httpbin.org/get'
#request = "GET /get HTTP/1.1\r\nHost: www.httpbin.org" + "\r\n\r\n"
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#geturl = URL.split('/')
#print(URL)
#surl = geturl[0]
#s.connect(('www.httpbin.org', 80))
#s.sendall(request.encode())
#result = s.recv(1024)
#abc = result.decode()
#body = abc.split('\r\n\r\n')
#print('Output Get with Verbose : \n', result.decode())
#s.close()
#import argparse

#argParser = argparse.ArgumentParser()

#argParser.add_argument("-v", "--verbose", action='store_true',help="name of the user")
#argParser.add_argument("-n", "--"
#args = argParser.parse_args()

#print(args.verbose)
# display a friendly message to the user
#print("Hi  {},!".format(args["name"],))

#argParser.add_argument('req_type', type=str, help="GET/POST")
#argParser.add_argument('-v', "--verbose", action='store_true', help="Increase output ")
#argParser.add_argument('-s', '--header', action='append', help="Headers to HTTP Request with the format")
#argParser.add_argument('-d', '--data', action='store', help="An inline data to the body HTTP POST request")
#argParser.add_argument('-f', '--file', action='store', help="Use -f filename")
#argParser.add_argument('-o', '--optional', action='store', help="Write Body of Response to File" )
#argParser.add_argument('URL', type=str, help='Enter the URL ')
#args = argParser.parse_args()
#print(args.req_type)