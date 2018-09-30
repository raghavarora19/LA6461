import socket
import argparse


def get(verbose,header,optional,URL):
    request = "GET / HTTP/1.0\r\nHost: "+ URL + "\r\n\r\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.google.com", 80))
    s.sendall(request.encode())
    result = s.recv(1024)
    abc = result.decode()
    body = abc.split('\r\n\r\n')  # For Verbose
    if verbose == True:
        print('Output Get with Verbose : \n', result.decode())
    else:
        print('Output Get w/o Verbose : \n ', body[1])
    s.close()


def post(verbos,header,data,file,optional,URL):
 host = "www.httpbin.org"
 port = 80
 if(data == None):
     data = ""
 print(header)
 head= ""
 for i in header:
    # print(i)
     head= head + str(i) + " \r\n"

 #head='\r\n'.join(header)
 print(head)

 body = '' + data + ''
 lbody=len(body)

 headers = """\
POST /post HTTP/1.1\r
Content-Type: application/json\r
Content-Length: """ + str(lbody) + """\r
Host: www.httpbin.org/post\r
Connection: close\r
\n""" + head + """
\r\n """

 body_bytes = body.encode('ascii')
 header_bytes = headers.format(
    content_type="application/json",
    content_length=len(body_bytes),
    host=str(host) + ":" + str(port)
 ).encode('iso-8859-1')

 payload = header_bytes + body_bytes
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect(("www.httpbin.org", 80))
 s.sendall(payload)
 payload = s.recv(1024)
 abc = payload.decode()
 body = abc.split('\r\n\r\n')  # For Verbose
 if verbos == True:
        print('\n Output:\n', payload.decode())
 else:
        print('\n Output:\n', body[1])
 s.close()



def main():

    argParser = argparse.ArgumentParser()

    argParser.add_argument('req_type', type=str, help="GET/POST")
    argParser.add_argument('-v', "--verbose", action='store_true', help="Increase output ")
    argParser.add_argument('-s', '--header', action='append', help="Headers to HTTP Request with the format")
    argParser.add_argument('-d', '--data', action='store', help="An inline data to the body HTTP POST request")
    argParser.add_argument('-f', '--file', action='store', help="Use -f filename")
    argParser.add_argument('-o', '--optional', action='store', help="Write Body of Response to File" )
    argParser.add_argument('URL', type=str, help='Enter the URL ')
    args = argParser.parse_args()
    #print("Result : ", args.verbose,args.header,args.data,args.file,args.optional,args.URL)
    if args.req_type == 'get' and 'GET':
        if args.header == None:
            nhead=" "
            get(args.verbose, nhead, args.optional, args.URL)
        else : get(args.verbose, args.header, args.optional, args.URL)

    elif args.req_type == 'post' and 'POST':
        if args.header == None :
            nhead=" "
            post(args.verbose, nhead, args.data, args.file, args.optional, args.URL)
        else : post(args.verbose, args.header, args.data, args.file, args.optional, args.URL)




main()


