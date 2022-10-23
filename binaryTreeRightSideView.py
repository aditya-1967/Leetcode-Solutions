# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        depth = 0
    
        def rightview(root, depth):
            if not root:
                return
            if depth == len(res):
                res.append(root.val)
            rightview(root.right, depth+1)
            rightview(root.left, depth+1)
            
    
        rightview(root, depth)
        return res
