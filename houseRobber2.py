# 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums)+1)
        
        def chor(n):
            if n == 1:
                return nums[0]
            dp[n-1] = 0
            dp[n-2] = nums[n-2]
            for i in range(n-3, -1, -1):
                dp[i] = max(dp[i+1],dp[i+2]+nums[i])
            val1 = dp[0]
            dp[n] = 0    
            dp[n-1] = nums[n-1]
            for i in range(n-2, 0, -1):
                dp[i] = max(dp[i+1],dp[i+2]+nums[i])
            val2 = dp[1]
            return max(val1, val2)
        return chor(len(nums))
