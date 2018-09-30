import argparse

argParser = argparse.ArgumentParser()

argParser.add_argument("-v", "--verbose", action='store_true',help="name of the user")
#argParser.add_argument("-n", "--"
args = argParser.parse_args()

print(args.verbose)
# display a friendly message to the user
#print("Hi  {},!".format(args["name"],))
