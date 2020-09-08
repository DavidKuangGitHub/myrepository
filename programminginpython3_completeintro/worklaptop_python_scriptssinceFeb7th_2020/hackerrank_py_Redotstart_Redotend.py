"""hackerrank_py_Redotstart_Redotend.py
#>>>import re
#>>>m = re.search(r'\d+','1234')
#>>>m.end()
#>>>4
#>>>m.start()
#>>>0
Example: Input: aaadaa
                aa
        Output: (0, 1)
                (1, 2)
                (4, 5)
"""
import re

s = input()
k = input()
index = 0
if re.search(k, s):
    while index + len(k) < len(s):
        m = re.search(k, s[index:])  # begins search with new index
        print("({0}, {1})".format(index + m.start(), index + m.end() - 1))
        index += m.start() + 1  # assign new index by +1
else:
    print((-1, -1))
