"""leetcode_pythonq_169_MajorityElement.py"""
"""Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2]
You may assume that the array is non-empty and the majority element always exist in the array.
Example1. Input; [3,2,3]
Output: 3
Example2. Input; [2,2,1,1,1,2,2]
Output: 2"""
class SolutionMar302020:
  def majorityElement(self, nums) -> int:
    a = list(set(nums))
    cnt = 0
    while cnt < len(a):
      if nums.count(a[cnt]) > len(nums)/2:
        return a[cnt]
      cnt +=1

"""instaceSolutionMar302020 = SolutionMar302020()
nums_M302020 =  [3,2,3]
nums_M302020 =  [2,2,1,1,1,2,2]
print("ResultOfThisSolution = ", instaceSolutionMar302020.majorityElement(nums_M302020)) 
"""
