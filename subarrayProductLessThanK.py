# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, res, product = 0, 0, 1
        for right in range(len(nums)):
            product *= nums[right]
            if product >= k:
                while product >= k and left <= right:
                    product /= nums[left]
                    left += 1
            res += right - left + 1
        
        return res
