"""leetcode_MaximumSubarray_same_structure_asjava.py"""
"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example: Input: [-1,1,-3, 4,-1,2,1,-5,4] Output: 6 Explanation: [4,-1,2,1] has the largest sum that is 6"""
class Solution(object):
    def getMaximumSubarray(self, nums):
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        mx = nums[0]
        curr_mx = nums[0]
        for i in range(1,len(nums)):
            curr_mx = max(nums[i], curr_mx + nums[i])
            mx = max(mx, curr_mx)
        return mx

mySolution = Solution()
myNums = [-1,1,-3,4,-1,2,1,-5,4]
print("Sum of the maximum subarray = ", mySolution.getMaximumSubarray(myNums))
