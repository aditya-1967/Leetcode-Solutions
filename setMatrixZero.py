# 73. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZ = False
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZ = True
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowZ:
            for c in range(cols):
                matrix[0][c] = 0
