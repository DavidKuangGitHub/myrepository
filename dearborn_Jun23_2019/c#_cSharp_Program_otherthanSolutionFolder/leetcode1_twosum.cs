/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
*/
using System;
using System.Collections.Generic;

namespace ConsoleApp1csharpApr19_2021
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World DK latest updates on May 17, 2021!");
            int[] inputArray = { 3, 3 } /*{ 3, 2, 4 }*/ /*{ 2, 7, 11, 15 }*/;
            int target = 6 /*6*/ /*9*/;
            int[] vs = TwoSum(inputArray, target);
            int i = 0;
            foreach (var item in vs)
            {
                Console.WriteLine("outputArray[" +i+"] = "+ item.ToString());
                i++;
            }
            Console.ReadLine();
        }

        private static int[] TwoSum(int[] nums, int target)
        {
            var dict = new Dictionary<int, List<int>>();
            for (int i = 0; i < nums.Length; i++)
            {
                if (!dict.ContainsKey(nums[i]))
                    dict.Add(nums[i], new List<int>());
                dict[nums[i]].Add(i);
            }
            for (int i = 0; i < nums.Length; i++)
            {
                if (dict.ContainsKey(target - nums[i]))
                {
                    var li = dict[target - nums[i]];
                    for (int j = 0; j < li.Count; j++)
                    {
                        if (li[j] != i)
                        {
                            return new int[] { i, li[j] };
                        }
                    }
                }
            }
            return new int[0];
        }
    }
}
