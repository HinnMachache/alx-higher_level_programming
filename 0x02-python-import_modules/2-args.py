#!/usr/bin/python
if __name__ = "__main__":
    """List the Argument Passed"""
    import sys
    if (sys.argv < 2):
        print("0 arguments.")
    else:
        argv_list = list(sys.argv)
        argv_list.pop(0)
        argv_len = len(argv_list)
        print("{:n} arguments.".format(argv_len))
        i = 1
        for word in argv_list:
            print("{:n}: {}".format(i, word))
            i += 1