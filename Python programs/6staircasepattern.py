#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        s='#'*i
        #print(s.ljust(n))
        print(s.rjust(n))

if __name__ == '__main__':
    n = int(input("Enter "))

    staircase(n)
