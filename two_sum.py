'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        n = len(nums)
        i = 0
        while (i < n):
            j = i+1;
            while (j < n):
                if ( nums[i] + nums[j] == target):
                    output.append(i)
                    output.append(j)
                j+=1
            i +=1
        return output
