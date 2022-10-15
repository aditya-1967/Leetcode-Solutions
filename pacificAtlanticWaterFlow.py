# 417. Pacific Atlantic Water Flow
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        que1 = deque()
        for i in range(m):
            que1.append((i, 0))
        for j in range(n):
            que1.append((0, j))
        def bfs(que):
            visited = set()
            while que:
                i,j = que.popleft()
                if (i,j) in visited: continue
                visited.add((i,j))
                for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                    if 0 <= i + di < m and 0 <= j + dj < n:
                        if heights[i][j] <= heights[i+di][j+dj]:
                            que.append((i+di,j+dj))
            return visited
        que2 = deque()
        for i in range(m):
            que2.append((i,n-1))
        for j in range(n):
            que2.append((m-1,j))
        return list(bfs(que1) & bfs(que2))
