#!/usr/bin/python3

import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  
    return result

if __name__ == "__main__":
    try:
        
        if len(sys.argv) != 2:
            print("Usage: ./factorial.py <non-negative integer>")
        else:
            number = int(sys.argv[1])
            if number < 0:
                print("Please provide a non-negative integer.")
            else:
                f = factorial(number)
                print(f)
    except ValueError:
        print("Please provide a valid integer.")

