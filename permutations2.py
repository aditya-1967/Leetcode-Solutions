# 47. Permutations II
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = (list(permutations(nums)))
        for item in l:
            item = list(item)
            ans.append(item)
        res = []
        for i in ans:
            if i not in res:
                res.append(i)
        return res
