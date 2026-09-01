class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        low=0
        high=len(mat[0])-1
        # peak_element=-1

        while low <=high :
            maxx=-1
            mid=low + ((high-low)//2)
            for i in range (len(mat)):
                if mat[i][mid] > maxx:
                    maxx=mat[i][mid]
                    mid_index=i

            prev=-1
            after=-1
            if mid > 0:
                prev = mat[mid_index][mid - 1]
            if mid < len(mat[0]) - 1:
                after = mat[mid_index][mid + 1]

            if prev < maxx and maxx > after:
                # peak_element = maxx
                return (mid_index,mid)
            elif prev > maxx:
                high = mid - 1
            else:
                low = mid + 1
            
        return (-1,-1)