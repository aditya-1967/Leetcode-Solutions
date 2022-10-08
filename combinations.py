# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def helper(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return 
            for i in range(start, n+1):
                curr.append(i)
                helper(i+1, curr)
                curr.pop()
        
        helper(1, [])
        return res
