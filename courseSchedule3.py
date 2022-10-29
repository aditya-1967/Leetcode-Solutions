# 630. Course Schedule III
# There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.
# You will start on the 1st day and you cannot take two or more courses simultaneously.
# Return the maximum number of courses that you can take.

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        A, curr = [], 0
        for dur, ld in courses:
            heapq.heappush(A,-dur)
            curr += dur
            if curr > ld: curr += heapq.heappop(A)
        return len(A)
