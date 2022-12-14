# 74. Search a 2D Matrix
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        for row in matrix:
            for element in row:
                if element == target:
                    found = True
                    break
        return found
