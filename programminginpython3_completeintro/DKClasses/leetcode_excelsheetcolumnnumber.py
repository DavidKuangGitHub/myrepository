#leetcode_excelsheetcolumnnumber.py
#Given a column title as appear in an Excel sheet, return its corresponding column number
#For example: A->1, B->2, C->3, ..., Z->26, AA-> 27, AB-> 28, ...
#Example (1) Input: "B"  Output: 2  (2) Input: "AB"  Output: 28 (3) Input: "ZY"  Output: 701
class Solution(object):
    def titleToNumber(self, s):
        """   :type s:str
              :rtype: int
              A-1
              AA -> 27 because 26power(1)+1
              AAA -> 703 because 26 power(2)+1 
                Expectation is 704 when entering AAB
              """
        if len(s) == 1:
            return ord(s) - ord('A')+1
        else: 
            return (ord(s[0]) - ord('A') +1 )* pow(26, len(s) -1) + self.titleToNumber(s[1:])
            
mySolution = Solution()
"""print(mySolution.titleToNumber('A'))
print(mySolution.titleToNumber('AB'))"""
print(mySolution.titleToNumber('AAB'))
