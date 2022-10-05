# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        max = 0
        for key, value in freq.items():
            if freq[key] > max:
                max = freq[key]
        
        for key, value in freq.items():
            if freq[key] == max:
                return key
