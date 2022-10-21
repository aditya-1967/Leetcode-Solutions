# 210. Course Schedule II
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        res = []
        visited, cycle = set(), set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return res
