#leetcode_reverseString.py
#Requirements: Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
#Example: Input  s= abcdefg  k=2
#Output: bacdfeg

class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        #for i in xrange(0, len(a), 2*k):
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
        #return("testing")
        
mySolution = Solution()
print(mySolution.reverseStr("abcdefg", 2))
