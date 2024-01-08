#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        first_character = None
        str_len = 0
    else:
        first_character = sentence[0]
        str_len = len(sentence)
    return (str_len, first_character)
