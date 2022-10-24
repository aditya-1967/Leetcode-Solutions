# 654. Maximum Binary Tree
# You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        stack = []
        last = None
        
        for num in nums:
            while stack and stack[-1].val < num:
                last = stack.pop()
            
            node = TreeNode(num)
            if stack:
                stack[-1].right = node
            if last:
                node.left = last
            stack.append(node)
            last = None
        
        return stack[0]
