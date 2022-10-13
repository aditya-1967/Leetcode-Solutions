# 673. Number of Longest Increasing Subsequence
# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n)
        count = [1] * (n)
        
        maximum = 1
        
        for i in range(n):
            for j in range(i):
                if (nums[j] < nums[i]) and (1 + dp[j] > dp[i]):
                    dp[i] = 1 + dp[j]
                    count[i] = count[j]
                elif (nums[j] < nums[i]) and (1 + dp[j] == dp[i]):
                    count[i] += count[j]
            maximum = max(maximum, dp[i])
        
        ans = 0
        for i in range(n):
            if dp[i] == maximum:
                ans += count[i]
        
        return ans
