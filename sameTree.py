# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        
        def preorder(root, res):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)
            
        preorder(p, res1)
        preorder(q, res2)
        
        return res1 == res2
