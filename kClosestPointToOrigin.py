# 973. K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        distance = []
        for i in range(len(points)):
            d = ((points[i][0] - origin[0])**2 + (points[i][1] - origin[1])**2)**0.5
            distance.append([d, points[i]])
        distance.sort()
        # print([distance[0][1]])
        ans = []
        for i in range(k):
            ans.append(distance[i][1])
        return ans
