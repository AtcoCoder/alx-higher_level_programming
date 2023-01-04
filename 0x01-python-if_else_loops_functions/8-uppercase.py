#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        code_num = ord(str[i])
        if code_num > 96 and code_num < 123:
            code_num = (ord(str[i]) - 32)
        print("{:c}".format(code_num), end='')
    print()
