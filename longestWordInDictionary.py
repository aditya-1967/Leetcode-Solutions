# 720. Longest Word in Dictionary
# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
# Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.val = ''           

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.val = word     
    
    def bfs(self):         
        q = [self.root]
        res = ''
        while q:
            cur = q.pop(0)
            for child in cur.children.values():     
                if child.endOfWord:                 
                    q.append(child)
                    if len(child.val) > len(res):
                        res = child.val
        return res
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()        
        trie = Trie()       
        for word in words:  
            trie.addWord(word)
        
        return trie.bfs()   
