# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            copy = Node(node.val)
            hashmap[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        
        return dfs(node) if node else None
