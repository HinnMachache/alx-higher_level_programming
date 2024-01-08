def divisible_by_2(my_list=[]):
    event_list = []
    for num in my_list:
        if num % 2 == 0:
            event_list.append(True)
        else:
            event_list.append(False)
    return event_list
