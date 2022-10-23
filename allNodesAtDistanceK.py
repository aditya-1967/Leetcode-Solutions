# 863. All Nodes Distance K in Binary Tree
# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
# You can return the answer in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.right:
                queue.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)
            
            if node.left:
                queue.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
        
        q = collections.deque([target])
        distance = 0
        result = []
        visited = set()
        visited.add(target)
        
        while q and distance <= k:
            for _ in range(len(q)):
                node = q.popleft()
                if distance == k:
                    result.append(node.val)
                
                for neigh in graph[node]:
                    if neigh not in visited:
                        q.append(neigh)
                        visited.add(neigh)
            distance += 1
        
        return result
