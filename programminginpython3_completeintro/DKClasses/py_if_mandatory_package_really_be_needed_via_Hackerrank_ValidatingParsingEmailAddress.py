#import sys
#py_if_mandatory_package_really_be_needed_via_Hackerrank_ValidatingParsingEmailAddress.py
#Example:
#2
#DEXTER <dexter@hotmail.com>
#VIRUS <virus!@variable.:p>
#Example Output:
#DEXTER <dexter@hotmail.com>
#import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)
