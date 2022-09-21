import operator
import argparse
import sys
# parsing the args in a manner [keyword] [number] [number]
parser = argparse.ArgumentParser(description='А python-script that performs the standard math functions on the data')
parser.add_argument('function', help='function name')
parser.add_argument('first', help='first number of a problem')
parser.add_argument('second', help='second number of a problem')
args, unknown = parser.parse_known_args()
try:
    first = float(args.first)
    second = float(args.second)
except ValueError:
    print("Wrong type of operands, must be a real number!")
    sys.exit()
dictionary = {  # we create a dictionary to swap the keywords for real functions
    "add": "operator.add(first, second)",
    "sub": "operator.sub(first, second)",
    "mul": "operator.mul(first, second)",
    "div": "operator.truediv(first, second)"
}
if args.function in dictionary.keys():
    try:
        print(eval(dictionary[args.function]))
    except ZeroDivisionError:
        print("Division by zero!")
        sys.exit()
else:
    print('The operator is incorrect')  # if the function does not exist in dictionary

