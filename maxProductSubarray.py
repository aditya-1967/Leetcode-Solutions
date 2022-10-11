# 152. Maximum Product Subarray
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmin, currmax = 1, 1
        for n in nums:
            if n == 0:
                currmin, currmax = 1, 1
                continue
            temp = currmax*n
            currmax = max(currmax*n, currmin*n, n)
            currmin = min(temp, currmin*n, n)
            res = max(res, currmax)
        return res
