# 437. Path Sum III
# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        dick = {0: 1}
        
        def helper(root, prevSum):
            if not root:
                return 
            currSum = prevSum + root.val
            x = currSum - targetSum
            if x in dick:
                self.count += dick[x]
            if currSum in dick:
                dick[currSum] += 1
            else:
                dick[currSum] = 1
            helper(root.left, currSum)
            helper(root.right, currSum)
            dick[currSum] -= 1
        helper(root, 0)
        
        return self.count
            
