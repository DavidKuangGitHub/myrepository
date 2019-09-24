import math, os, random, re, sys

#Task: Read tow integers from STDIN and print three lines where: (1) 1st line contains the sum of the two numbers; (2) 2nd line contains the difference of the two numbers (first - second) (3) 3rd line contains the product of the two numbers. 
#Example 3  2 the output should be 5 (3+2)  1 (3-2)  6(3*2)
print("Enter 2 integers equal to or more than 1 but less than 10power(10) pls Note: line by line  ")
a = int(input())
b = int(input())
print("\nResult:")
#print('{0}  \n{1} \n{2}'.format((a + b), (a - b), (a*b)))
print('{0} + {1} = {2}'.format(a, b, (a + b ) ))
print('{0} - {1} = {2}'.format(a, b, (a - b ) ))
print('{0} X {1} = {2}'.format(a, b, (a * b ) ))
