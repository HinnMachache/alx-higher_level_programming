#!/usr/bin/python3
if __name__ == "__main__":
    """Handles diiferent operations"""
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:n} + {:n} = {:n}".format(a, b, add(a, b)))
    print("{:n} - {:n} = {:n}".format(a, b, sub(a, b)))
    print("{:n} * {:n} = {:n}".format(a, b, mul(a, b)))
    print("{:n} / {:n} = {:n}".format(a, b, div(a, b)))
