#! /bin/python

import math, os, random, re, sys

'''Problem Rank#635997 Task: Given an integer n, perform the following conditional actions: (1) if n is odd, print Weird 
(2) If n is even,   (a) and in the inclusive range of 2 to 5, print Not Weird 
                    (b) and in the inclusive range of 6 to 20, print Weird
                    (c) greater than 20, print Not Weird '''

N = int(input().strip())

if N % 2 == 1 or N >= 6 and N <= 20:
    print("Weird")
elif N >= 2 and N <= 5 or N >= 20:
    print("Not Weird")