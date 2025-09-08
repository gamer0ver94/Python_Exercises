import sys

assert len(sys.argv) < 3 , "more than one argument is provided"
assert sys.argv[1].isdigit(), "argument is not an integer"

if int(sys.argv[1]) % 2 == 0:
    print("I'am Even.")
else:
    print("I'am Odd.")


