# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        
        def diameter(root):
            if not root:
                return -1
            
            l = diameter(root.left)
            r = diameter(root.right)
            maxi[0] = max(maxi[0], 2+l+r)
            
            return 1 + max(l, r)
        
        diameter(root)
        return maxi[0]
