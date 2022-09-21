import sys
argument_number = len(sys.argv)
arguments_line = ""
for a in range(1, argument_number): # build a line from args list
    arguments_line += sys.argv.pop(1)
    arguments_line += " "
print(arguments_line)
try:
    result = eval(arguments_line)
    print('True,', result)
except SyntaxError:
    print("False, Statement is incorrect")
except ZeroDivisionError:
    print("False, Division by zero")
