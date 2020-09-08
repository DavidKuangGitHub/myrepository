"""leetcode_pyq_1_twosum.py
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Example1:Input: nums=[2,7,11,15] target = 9 Output: [0,1] as 2+7=9
Example2:Input: nums=[3,2,4] target = 6 Output: [1,2] as 2+4=6
"""


class Solution_leetcode_q1_Sep82020:
    def twoSum(self, nums, target):
        storage = {}
        for i, elem in enumerate(nums):
            if target - elem in storage:
                return [storage[target - elem], i]
            storage[elem] = i
        return []


mySolution_leetcode_q1_Sep82020 = Solution_leetcode_q1_Sep82020()
nums = [2, 7, 11, 15]
mytarget = 9
"""nums = [3,2,4]
mytarget = 6"""
print("Result/Output = ", mySolution_leetcode_q1_Sep82020.twoSum(nums, mytarget), "!")