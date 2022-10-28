# 828. Count Unique Characters of All Substrings of a Given String
# Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
# For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
# Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.
# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {c: [-1, -1] for c in ascii_uppercase}
        res = 0
        for i, c in enumerate(s):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(s) - j) * (j - k)
        return res % (10**9 + 7)
