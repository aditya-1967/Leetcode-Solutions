# 90. Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, curSubset):
            ans.append(curSubset[::])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue  
                curSubset.append(nums[i])
                dfs(i + 1, curSubset)
                curSubset.pop()

        nums.sort()
        ans = []
        dfs(0, [])
        return ans
