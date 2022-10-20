# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dick = {}
        res = 0
        left = 0
        for i in range(len(s)):
            dick[s[i]] = 1 + dick.get(s[i], 0)
            while (i-left+1) - max(dick.values()) > k:
                dick[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res
