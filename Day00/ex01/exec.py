import sys

print ("test")
arguments = sys.argv[1:]
arguments = arguments[::-1]

for x in range(len(arguments)):
    arguments[x] = arguments[x] [::-1]
    
    print(arguments[x].swapcase(),end='')
    
    if x + 1 != len(arguments):
        print(" ", end='')

