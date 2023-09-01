#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    x = 0
    n_bin = bin(n)[2:]
    max_sequence = max(n_bin.split('0'))
    print(len(max_sequence))
