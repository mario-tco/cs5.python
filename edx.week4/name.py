import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#Slice example. -1 removes the last element:
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)