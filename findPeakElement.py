# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n = len(nums)
        left = 0
        right = n-1
                
        while  left <= right:
            mid = left + (right-left)//2
            if (mid==0 or nums[mid-1] < nums[mid]) and (mid==n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif (mid!=0 and nums[mid-1] > nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
