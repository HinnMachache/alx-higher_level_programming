#!/usr/bin/python3
if __name__ == "__main__":
    """List the Argument Passed"""
    from sys import argv
    if (len(argv) < 2):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(len(argv) - 1, argv[1]))
        exit()
    else:
        argv.pop(0)
        print("{:n} arguments:".format(len(argv)))
        num = 1
        for index in range(0, len(argv)):
            print("{:n}: {}".format((num), argv[index]))
            num += 1
