# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack and c == '#':
                    stack.pop()

            return stack

        stack1 = helper(s)
        stack2 = helper(t)
        if stack1 == stack2:
            return True
        else:
            return False
