# 995. Minimum Number of K Consecutive Bit Flips
# You are given a binary array nums and an integer k.
# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
# A subarray is a contiguous part of an array.

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        cur, res, n = 0, 0, len(nums)
        for i in range(len(nums)):
            if i >= k and nums[i - k] > 1:
                nums[i - k] -= 2
                cur -= 1
            if cur & 1 ^ nums[i] == 0:
                if i + k > len(nums):
                    return -1
                nums[i] += 2
                cur += 1
                res += 1
        return res
