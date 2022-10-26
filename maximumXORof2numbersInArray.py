# 421. Maximum XOR of Two Numbers in an Array
# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, output = 0, 0
        
        for i in range(32, -1, -1):
            mask = mask | 1 << i
            found = set([n & mask for n in nums])
            
            temp = output | 1<<i
            
            for f in found:
                if f ^ temp in found:
                    output = temp
        
        return output
