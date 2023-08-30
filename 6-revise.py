#!/bin/python3

def print_even_odd_characters(s):
     # Get even-indexed characters
    x = s[::2] 
    # Get odd-indexed characters
    y = s[1::2] 
    print(x, y)

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        print_even_odd_characters(s)
