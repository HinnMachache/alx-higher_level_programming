def no_c(my_string):
    my_str = []
    for ch in my_string:
        if (ch != 'c' and ch != 'C'):
            my_str.append(ch)
    return ''.join(my_str)
