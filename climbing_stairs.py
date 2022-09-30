# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def func(n):
            if n <= 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = func(n-1) + func(n-2)
            return dp[n]
        return func(n)
