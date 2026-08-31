class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        # row=-1
        # col=-1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else: #if matrix[i][j]==target:
                # row=i 
                # col=j
                return True
        return False
