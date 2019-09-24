import math, os, random, re, sys

#py_Division_via_hackerranker_problem  Task: Read two integers and print two lines. The 1st line should contain integer divison a /b and the 2nd line should contain float division a.|. b. There is no rounding or formatting operations needed. 
#Input Format: The 1st line contains the first integer a. The 2nd line contains the 2nd integer b
#Output Format: Print the two lines as described above.
#Example: 4
#4
#3
#Example Output: 
#1
#1.33333333333

print("Enter 2 integers:")
a = int(input())
b = int(input())

print("\nResults:")
print("{0} \n{1}".format((a // b ), ( a / b )))
