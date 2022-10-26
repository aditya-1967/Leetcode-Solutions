# 41. First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        for j in nums:
            if j == i:
                i += 1
        return i
