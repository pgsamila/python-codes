#!/bin/python3

#thi code is comitted by Amila Sampath for
#for group code bank


import random
import sys
import os


def is_leap(y):
    if (y % 4 == 0 and y%100 != 0) or (y%100 == 0 and y % 400 == 0):
        k = True
    else:
        k = False
    return k

year = int(input())
print(is_leap(year))