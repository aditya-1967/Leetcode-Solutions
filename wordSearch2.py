# 212. Word Search II
# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

class TrieNode:
    def __init__(self, val: str = None, parent: Optional['TrieNode'] = None):
        self.children = {}
        self.val = val
        self.parent = parent
        self.word = None
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    
    def addWord(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(val=c, parent=node)
            node = node.children[c]
        node.word = word
    
    def prune(self, node: TrieNode):
        node.word = None
        child = node
        parent = child.parent
        while parent and len(child.children) == 0:
            del parent.children[child.val]
            child = parent
            parent = parent.parent
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        
        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            
            node = node.children[board[r][c]]
            
            if node.word:
                res.add(node.word)
                root.prune(node)
            
            if len(node.children) == 0:
                visit.remove((r, c))
                return
                    
                
            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)
            
            visit.remove((r, c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root.root)
        
        return list(res)
            
        
