import argparse

argParser = argparse.ArgumentParser()

#argParser.add_argument("-v", "--verbose", action='store_true',help="name of the user")
#argParser.add_argument("-n", "--"
#args = argParser.parse_args()

#print(args.verbose)
# display a friendly message to the user
#print("Hi  {},!".format(args["name"],))

argParser.add_argument('req_type', type=str, help="GET/POST")
#argParser.add_argument('-v', "--verbose", action='store_true', help="Increase output ")
#argParser.add_argument('-s', '--header', action='append', help="Headers to HTTP Request with the format")
#argParser.add_argument('-d', '--data', action='store', help="An inline data to the body HTTP POST request")
#argParser.add_argument('-f', '--file', action='store', help="Use -f filename")
#argParser.add_argument('-o', '--optional', action='store', help="Write Body of Response to File" )
#argParser.add_argument('URL', type=str, help='Enter the URL ')
args = argParser.parse_args()
print(args.req_type)