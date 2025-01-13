#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <integer>")
        sys.exit(1)

    print(" ".join(sys.argv[1:]))
