#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
if argc == 0:
    print("{} arguments.".format(argc))
elif argc == 1:
    print("{} argument:".format(argc))
else:
    print("{} arguments:".format(argc))
for arg_num in range(1, argc + 1):
    print("{}: {}".format(arg_num, sys.argv[arg_num]))
