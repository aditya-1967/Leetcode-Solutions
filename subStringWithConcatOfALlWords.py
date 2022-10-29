# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return self.helper(s, words)
        
    def helper(self, s, words):
        if not s or len(s) == 0 or not words or len(words) == 0:
            return []
        freq_words = Counter(words)
        word_length = len(words[0])
        total_words = len(words)
        res = []
        for i in range((len(s)-total_words*word_length)+1):
            seen = {}
            for j in range(total_words):
                wordIndex = i + j * word_length
                word = s[wordIndex:wordIndex + word_length]
                if word not in freq_words:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > freq_words.get(word, 0):
                    break
                if j + 1 == total_words:
                    res.append(i)
        return res
