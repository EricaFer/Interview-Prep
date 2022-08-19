'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

from operator import contains


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    for index, num in enumerate(nums):
        
        GoalNum = target - num
        
        if GoalNum in nums:
            
            SecondIndex = nums.index(GoalNum)

            if SecondIndex != index:

                break

    return [index,SecondIndex]

print(twoSum(nums = [3,3], target = 6))
