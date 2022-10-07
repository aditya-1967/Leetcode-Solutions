# 784. Letter Case Permutation
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        
        for c in s:
            temp = []
            if c.isalpha():
                for i in res:
                    temp.append(i + c.lower())
                    temp.append(i + c .upper())
            else:
                for i in res:
                    temp.append(i + c)
            res = temp
        
        return res
