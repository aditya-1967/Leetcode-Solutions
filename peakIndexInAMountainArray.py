# 852. Peak Index in a Mountain Array
# An array arr a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
#a rr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# You must solve it in O(log(arr.length)) time complexity.

class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
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
