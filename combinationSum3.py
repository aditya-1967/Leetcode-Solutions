# 216. Combination Sum III
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(curr, num, total):
            if len(curr) == k:
                if total == n:
                    res.append(curr)
                    return
            
            for i in range(num, 9+1):
                if total + i > n:
                    break
                dfs(curr + [i], i + 1, total + i)
        
        dfs([], 1, 0)
        return res
