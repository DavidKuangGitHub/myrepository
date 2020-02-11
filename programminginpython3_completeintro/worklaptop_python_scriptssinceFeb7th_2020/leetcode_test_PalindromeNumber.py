'''This is to determine whether an integer is a palindrome. Definition of palindrome: an integer when it reads the same backward as forward.
Example-1. Input: 121
Output: true
Example-2. Input: 10
Output: false
Example-5. Input: -121
Output: false
'''
class Solution02112020:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        last_index = len(sx) - 1
        for index, num in enumerate(sx):
            if num != sx[last_index - index]:
                return False
            if index >= last_index - index:
                return True

mySolution02112020 = Solution02112020()
print("Enter your integer that can be checked whether it is a palindrome or not:")
a=int(input())
#print(mySolution02112020.isPalindrome(a))
print('\nYou entered {0} thats with palindrome check result of {1}'.format(a, mySolution02112020.isPalindrome(a)))
