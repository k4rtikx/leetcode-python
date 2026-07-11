""" Do not return anything, modify matrix in-place instead. """
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = 1
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col = 0
                    else:
                        matrix[0][j] = 0

        for i in range(n-1, 0, -1):
            for j in range(m-1, 0, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        if col == 0:
            for i in range(n):
                matrix[i][0] = 0