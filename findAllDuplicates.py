# 442. Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        freq = {}
        for item in nums:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        for key, value in freq.items():
            if value > 1:
                ans.append(key)
        return ans
