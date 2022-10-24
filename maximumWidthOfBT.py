# 662. Maximum Width of Binary Tree
# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        q = collections.deque([(root,1)])
        result = []
        while q:  
            lenq = len(q) 
            first = None
            last = None

            for _ in range(lenq):  
                (node,id) = q.popleft() 
                if node.left:
                    q.append((node.left, 2*id))
                if node.right:
                    q.append((node.right,2*id+1))
                last = id
                if first is None:
                    first = id
                result.append(last-first+1)
        return max(result)
