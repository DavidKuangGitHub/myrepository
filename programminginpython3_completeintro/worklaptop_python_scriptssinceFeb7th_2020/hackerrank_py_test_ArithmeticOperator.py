'''Task: read two integers from STDIN and print three lines.
Requirements: 1. The first line contains the sum of the two numbers, first+second
2. The second line contains the difference of the two numbers you enter first-second
3. The third line contains the product of the two numbers   first*second
Input/Output Format: The first line contains the first integer a; The second line contains the second integer b.
Constraints: 1 <= a <= 10powerof10  , 1 <= b <= 10powerof10
Example:Input=>
3
2
Output=>
5
1
6
Because 5=3+2; 1=3-2; 6=3*2
'''
import math

print("Please enter two integers [0, 10powerof10]:")
a=int(input())
b=int(input())
print('\nAs per integers you entered, Here is the Results:\n{0}  \n{1} \n{2}'.format((a+b),(a-b),(a*b)))


