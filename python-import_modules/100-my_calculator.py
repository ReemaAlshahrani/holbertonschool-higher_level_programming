#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    sys_argv = __import__('sys').argv
    sys_exit = __import__('sys').exit

    if len(sys_argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys_exit(1)

    a = int(sys.argv[1])
    operator = sys_argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys_exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
