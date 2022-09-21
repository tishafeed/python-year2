import sys
try:
    print(eval(sys.argv[1]+sys.argv[2]+sys.argv[3]))  # will try to execute expression
except ZeroDivisionError:  # unless it's a division by zero
    print('Division by zero!')  # in this case we'll just tell the user
except Exception as ex:
    print(ex)

