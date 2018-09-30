import argparse

argParser = argparse.ArgumentParser()

argParser.add_argument("-v", "--verbose", required=,help="name of the user")
argParser.add_argument("-n", "--"
args = vars(argParser.parse_args())


# display a friendly message to the user
print("Hi  {},!".format(args["name"],))
