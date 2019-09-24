#import os
#py_Loops_via_hackerrank_com_ws.py Task: Read an integer N. For all non-negative integers i < N. print ipower(2), see the example for details.
#Input Format: The first and only line contains the integer, N
#Constraints: 1 <=N <=20
#Example:
#5
#Example Output:
#0
#1
#4
#9
#16

print("Enter one integer that equals to 1 or more than 1 less than 20 or equals to 20:")
a = int(input())

print("Results")
for i in range(a):
  print(i*i)
