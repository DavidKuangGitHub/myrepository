"""This is an demo of Sphinx Documentation applying for Python Doc String (DocStrings). 
   Program Name : leetcode_pythonq_53_MaximumSubarray.py
   Author       : David Kuang
   Create Date  : Aug 24, 2020
   Last Updated : Aug 25, 2020
   Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
   For example: Input [-2, 1, -3, 4, -1, 2, 1, -5, 4] Output: 6 because '4, -1, 2, 1' has the largest sum =6. 
   """
class Solution_Aug24_2020(object):
    def maxSubArray(self, nums):
        """
        This is a method that read an integer array, apply the algorithm, and return the largest sum value of contiguous subarray
        Parameters: 
        :type nums: List[int]
        :rtype    : int"""
        max_sum = nums[0]
        start = 0
        temp_sum = nums[0]
        for index in range(1, len(nums)):
            temp_sum += nums[index]
            if nums[index] > temp_sum:
                start = index
                temp_sum = nums[index]
            if temp_sum > max_sum:
                max_sum = temp_sum 
        return max_sum

"""mySolution_Aug24_2020 = Solution_Aug24_2020()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("ReturnValueOfmySolution_Aug24_2020 is ", mySolution_Aug24_2020.maxSubArray(nums),"!")"""
