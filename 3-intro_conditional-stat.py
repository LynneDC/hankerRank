#!/bin/python3

import math
import os
import random
import re
import sys

def solve_n(N):
    if N == 0:
        pass  
    if N % 2 == 0 and 2 <= N <= 5:
        print("Not Weird")
    if N % 2 == 0 and 6 <= N <= 20:
        print("Weird")
    if N % 2 == 0 and N > 20:
        print("Not Weird")
    else:
        if N % 2 != 0:
            print("Weird")

if __name__ == '__main__':
    N = int(input().strip())
    solve_n(N)
