# 113. Path Sum II
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        def dfs(root, path, total):
            if not root:
                return []
            
            total += root.val
            temp = path + [root.val]
            
            if root.left:
                dfs(root.left, temp, total)
            if root.right:
                dfs(root.right, temp, total)
            if not root.left and not root.right and total == targetSum:
                res.append(temp)
            
        
        dfs(root, [], 0)
        return res
