# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    nums_set = set(nums)
    res = [i for i in range(1, len(nums)+1) if i not in nums_set]
    return res
