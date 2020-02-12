'''leetcode_test_LongestCommonPrefix.py
To write a class/function/method to find the longest common prefix string amongst an array of strings
If there is no common prefix, return an empty string ""
Note: All given inputs are in lowercase letters a ~ z
Example1: Input: ["flower","flow","flight"]
Output: "fl"
Example2: Input: ["dog","racecar","car"]
Output: ""

'''
class Solution02122020(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        longest = strs[0]
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]

mySolution02122020 = Solution02122020()
print(mySolution02122020.longestCommonPrefix(["hello", "heabc", "hell"]))
