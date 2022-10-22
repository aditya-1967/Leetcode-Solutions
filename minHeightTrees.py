# 310. Minimum Height Trees
# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels. You can return the answer in any order.
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]
        
        neighbours = [set() for x in range(n)]
        
        for start, end in edges:
            neighbours[start].add(end)
            neighbours[end].add(start)
            
        leaves = []
        for i in range(n):
            if len(neighbours[i]) == 1:
                leaves.append(i)
        
        remain = n
        
        while remain > 2:
            remain -= len(leaves)
            temp = []
            for leaf in leaves:
                for neighbour in neighbours[leaf]:
                    neighbours[neighbour].remove(leaf)
                    if len(neighbours[neighbour]) == 1:
                        temp.append(neighbour)
            
            leaves = temp
        
        return leaves
