#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    meridian=s[-2:]
    if meridian=='PM' and s[:2]!='12':
        if s[:2]>'12':
            s=str(int(s[:2])-12)+s[2:]
        else:
            s=str(12+int(s[:2]))+s[2:]
    if meridian=='AM' and s[:2]=='12':
        s=('00'+s[2:])
    return s[:-2]
    #
    # Write your code here.
    #

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    #f.write(result + '\n')
    #f.close()
