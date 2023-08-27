#!/bin/python3

import math
import os
import random
import re
import sys

def multiples_n(n):
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n*i))

if __name__ == '__main__':
    n = int(input().strip())
    multiples_n(n)
