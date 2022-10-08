# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order

from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = (list(permutations(nums)))
        for item in l:
            item = list(item)
            ans.append(item)
        return ans
