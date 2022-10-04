# 112. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, currSum):
            if not root:
                return False
            currSum += root.val
            if not root.left and not root.right:
                return currSum == targetSum
            return (dfs(root.left, currSum) or dfs(root.right, currSum))
        
        return dfs(root, 0)
