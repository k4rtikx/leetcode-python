class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #conceptual=[ 1,3,5,7,10,11,16,20,23,30,34,60]
        # index:  0  1  2  3   4   5   6   7   8   9  10  11
        # value:  1  3  5  7  10  11  16  20  23  30  34  60
        low=0
        high = len(matrix) * len(matrix[0]) - 1 # 3 rows × 4 columns = 12 elements-1
        answer=False
        while low <=high:
            mid=low + ((high-low)//2)
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            value = matrix[row][col]

            if value ==target:
                answer= True
                break
            elif value >target:
                high=mid-1
            else:
                low= mid+1
        return answer
