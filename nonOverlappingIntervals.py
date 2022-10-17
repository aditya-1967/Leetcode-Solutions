# 435. Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]
        for i, j in intervals[1:]:
            if i >= prev_end:
                prev_end = j
            else:
                count += 1
                prev_end = min(j, prev_end)
        return count
