"""leetcode_lfpy_HouseRobber.py"""
"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight with alerting the police. 
Example1: 
Input: [1,2,3,1]
Output: 4, because 1(House#1)+3(House#3)
Example2: 
Input: [2,7,9,3,1]
Output: 12, because 2(House#1)+9(House#3)+1(House#5)
"""
class SolutionMar202020(object):
  def rob(self, nums):
    if len(nums) == 0:
      return 0
    if len(nums) == 1:
      return nums[0]
      
    d1 = max(nums[0], nums[1])
    d2 = nums[0]
    m = 0
    if len(nums) == 2:
      return d1
    for i in range(2, len(nums)):
      m = max(d1, d2 + nums[i])
      d2 = d1
      d1 = m
    return m
    
    
"""instanceOfSolutionMar202020 = SolutionMar202020()
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print("ResultOfThisSolution = ", instanceOfSolutionMar202020.rob(nums))
"""
