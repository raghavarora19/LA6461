import socket
import argparse


# Redirection -> TEST WITH URL www.amazon.org


def get(verbose, header, optional, URL):
    request = "GET / HTTP/1.0\r\nHost: " + URL + "\r\n\r\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    geturl = URL.split('/')
    surl = geturl[0]
    s.connect(("" + surl + "", 80))
    s.sendall(request.encode())
    result = s.recv(1024)
    abc = result.decode()
    body = abc.split('\r\n\r\n')
    redirectget(body, False, verbose, header, optional, URL)  # call to redirect function
    if optional:
        f1 = open(optional, "w+")
        f1.write(body[1])
        if verbose:
            print('Output Get wi'
                  'th Verbose + Body Output to file ' + optional + ': \n ', body[0])
            exit(0)
        else:
            exit(0)
    # For Verbose
    if verbose == True:
        print('Output Get with Verbose : \n', result.decode())
    else:
        print('Output Get w/o Verbose : \n ', body[1])

    s.close()


def post(verbos, header, data, file, optional, URL):
    if (data == None):
        data = ""
    if file:
        f1 = open(file, "r")
        read_file = f1.read()
        body = '' + data + ' ' + read_file + ''
    else:
        body = '' + data + ''

    host = URL
    port = 80
    head = ""
    for i in header:
        head = head + str(i) + " \r\n"

    lbody = len(body)
    surl = URL.split('/')
    shorturl = surl[0]
    longurl = '/'.join(surl[1:])


    headers = """\
POST http://""" + URL + """ HTTP/1.1\r
Content-Type: application/json\r
Content-Length: """ + str(lbody) + """\r
Host: """ + URL + """\r
Connection: close\r""" + """\n""" + head + """\r
"""
    if URL == "www.ptsv2.com/t/raghav/post":
        print(longurl)
        headers = """\
POST /""" + longurl + """ HTTP/1.1\r
Content-Type: application/json\r
Content-Length: """ + str(lbody) + """\r
Host: """ + shorturl + """\r
Connection: close\r""" + """\n""" + head + """\r
"""

    body_bytes = body.encode('ascii')
    header_bytes = headers.format(
        content_type="application/json",
        content_length=len(body_bytes),
        host=str(host) + ":" + str(port)
    ).encode('iso-8859-1')

    payload = header_bytes + body_bytes
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((shorturl, 80))
    s.sendall(payload)
    payload = s.recv(1024)
    abc = payload.decode()
    body = abc.split('\r\n\r\n')
    redirectput(body, True, verbos, header, data, file, optional, URL)  # For Verbose
    if optional:
        f2 = open(optional, "w+")
        f2.write(body[1])
        if verbos:
            print('Output Post with Verbose + Body Output to file ' + optional + ': \n ', body[0])
            exit(0)
        else:
            exit(0)
    if verbos == True:
        print('\rOutput with Verbose:\n', payload.decode())
    else:
        print('\rOutput w/o Verbose:\n', body[1])
    s.close()


def redirectget(payload, reqtype, verbose, header, optional, URL):
    payload[0]
    stat = payload[0].splitlines()
    status = stat[0].split()
    status_code = status[1]
    # print(int(status_code))
    if (int(status_code) >= 300) & (int(status_code) < 400):  # TEST WITH URL www.amazon.org
        print("You have been Redirected:", status_code)
        if reqtype == False:
            get(verbose, header, optional, 'www.google.com')
            exit(0)


def redirectput(payload, reqtype, verbose, header, data, file, optional, URL):
    payload[0]
    stat = payload[0].splitlines()
    status = stat[0].split()
    status_code = status[1]
    if (int(status_code) >= 300) & (int(status_code) < 400):
        print("You have been Redirected: ", status_code)
        if reqtype == True:
            post(verbose, header, data, file, optional, "www.httpbin.org/post")
            exit(0)


def main():
    argParser = argparse.ArgumentParser()

    argParser.add_argument('req_type', type=str, help="GET/POST")
    argParser.add_argument('-v', "--verbose", action='store_true', help="Increase output ")
    argParser.add_argument('-s', '--header', action='append', help="Headers to HTTP Request with the format")
    argParser.add_argument('-d', '--data', action='store', help="An inline data to the body HTTP POST request")
    argParser.add_argument('-f', '--file', action='store', help="Use -f filename")
    argParser.add_argument('-o', '--optional', action='store', help="Write Body of Response to File")
    argParser.add_argument('URL', type=str, help='Enter the URL ')
    args = argParser.parse_args()
    if args.data and args.file:
        print("Request format incorrect use one of -d or -f")
        exit(1)

    # print("Result : ", args.verbose,args.header,args.data,args.file,args.optional,args.URL)
    if args.req_type == 'get' and 'GET':
        if args.header == None:
            nhead = " "
            get(args.verbose, nhead, args.optional, args.URL)
        else:
            get(args.verbose, args.header, args.optional, args.URL)

    elif args.req_type == 'post' and 'POST':
        if args.header == None:
            nhead = " "
            post(args.verbose, nhead, args.data, args.file, args.optional, args.URL)
        else:
            post(args.verbose, args.header, args.data, args.file, args.optional, args.URL)


main()
