# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in s:
                j = 0
                while i+j in s:
                    j += 1
                ans = max(j , ans)
        return ans
