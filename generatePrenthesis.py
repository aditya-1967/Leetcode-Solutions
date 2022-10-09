# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []
        
        def helper(open, close):
            if open == close == n:
                res.append("".join(stack))
            
            if open < n:
                stack.append('(')
                helper(open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(')')
                helper(open, close + 1)
                stack.pop()
        
        helper(0, 0)
        return res
