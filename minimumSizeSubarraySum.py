# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, ans = 0, len(nums) + 1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                ans = min(ans, i-l+1)
                total -= nums[l]
                l += 1
        if ans == len(nums) + 1:
            return 0
        return ans
