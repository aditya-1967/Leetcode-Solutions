# 37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    def solve(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    for c in range(1,9+1):
                        if self.isvalid(board,i,j,c):
                            board[i][j]=str(c)
                            if self.solve(board)==True:
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
    def isvalid(self,board,row,col,c):
        for i in range(0,9):
            if board[i][col]==str(c):
                return False
            if board[row][i]==str(c):
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==str(c):
                return False
        return True
