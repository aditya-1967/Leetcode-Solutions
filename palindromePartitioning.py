# 131. Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
