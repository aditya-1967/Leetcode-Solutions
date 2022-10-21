# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        l = [[value, key] for key, value in freq.items()]
        print(l)
        l.sort()
        print(l)
        string = ""
        for i in l:
            string += i[1]*i[0]
        print(string)
        print(string[::-1])
        return string[::-1]
