#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    from calculator_1 import add, sub, mul, div

    if (len(sys.argv) - 1 != 3):
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if (sys.argv[2] not in '+-*/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operations = {"+":add, "-": sub, "*": mul, "/": div}

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}". format(a, sys.argv[2], b, operations[sys.argv[2]](a, b)))


