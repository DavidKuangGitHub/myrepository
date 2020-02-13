'''leetcode_test_removeduplicatesfromsortedarray.py
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Don't allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example1: Given nums = [1,1,2]. Length=2, 1, 2
Example2: Given nums = [0,0,1,1,1,2,2,3.3,4]. Length=5,and 0, 1, 2,3,4
'''


class SolutionFeb13c2020(object):
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1
        idx = 1
        while idx < len(nums):
            if nums[idx - 1] == nums[idx]:
                nums.pop(idx)
                idx -= 1
            idx += 1
        return len(nums)


'''instanceOfSolutionFeb13c2020 = SolutionFeb13c2020()
nums = [1, 1, 2]
print(instanceOfSolutionFeb13c2020.removeDuplicates(nums))'''
