def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            element = my_list[i]
        except IndexError:
            continue
        else:
            print(element, end="")
            count += 1
    print()
    return count
