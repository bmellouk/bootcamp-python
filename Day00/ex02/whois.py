import sys

if len(sys.argv) > 1 :

    if len(sys.argv) != 2 :
        print("AssertionError: more than one argument are provided")
        exit()

    num = sys.argv[1]; 

    if num.isnumeric() == False :
        print('AssertionError: argument is not integer')
    else:
        if int(num) == 0:
            print("I'm Zero.") 
        elif int(num)% 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd.")
