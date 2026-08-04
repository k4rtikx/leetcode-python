class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        left =0
        right =m-1
        top = 0
        bottom = n-1
        ans=[]
        while left <= right and top <= bottom:
            for i in range (left,right+1):
                num=matrix[top][i]
                ans.append(num)
            top+=1
            for i in range(top,bottom+1):
                num=matrix[i][right]
                ans.append(num)
            right-=1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    num = matrix[bottom][i]
                    ans.append(num)
                bottom -=1
            if left <= right:
                for i in range (bottom , top-1,-1):
                    num = matrix[i][left]
                    ans.append (num)
                left+=1
        return ans