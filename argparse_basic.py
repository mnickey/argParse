""" positional arguments """
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
# 					type=int)
# args = parser.parse_args()
# print args.square**2

""" optional arguments """
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print "verbosity turned on"

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbosity",
# 					help="increase output verbosity", 
# 					action="store_true")
# args = parser.parse_args()
# if args.verbosity:
#     print "verbosity turned on"

""" positional and optional arguments """ 
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print "the square of {} equals {}".format(args.square, answer)
# else:
#     print answer

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print "the square of {} equals {}".format(args.square, answer)
# elif args.verbosity == 1:
#     print "{}^2 == {}".format(args.square, answer)
# else:
#     print answer

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print "the square of {} equals {}".format(args.square, answer)
# elif args.verbosity == 1:
#     print "{}^2 == {}".format(args.square, answer)
# else:
#     print answer


import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print answer
elif args.verbose:
    print "{} to the power {} equals {}".format(args.x, args.y, answer)
else:
    print "{}^{} == {}".format(args.x, args.y, answer)


"""
How do you create an argument parser?
	import argparse
	parser.add_argument("-x". "--Xtra_log_name", action="store_true")
How do you find out the command line arguments an app using argparse takes?
	run the script with a '--help' or '-h' flag
What is the difference between a positional and an optional argument?
	a positional argument will run based on it's position in the command execution
	an optional argument will execute 'optional' commands but do not have to be present 
	for the command line to run
How would you add an optional argument for receiving an integer?
	add a type=int in the parser.add_argument line
What does the action parameter of add_argument do?
	action lines change the value from Null to what is passed in.
How do you add a default value for an argument?
	set a default=xxx in the parser.add_argument line 
"""