class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position=sorted(position)
        low = 1
        high= max(position)
        ans=-1
        while low <=high:
            mid=low + ((high-low)//2)
            cow=1
            least=position[0]
            for j in range(1,len(position)):
                if position[j] -least  >= mid :
                    cow +=1
                    least = position[j]
            if cow >= m :
                ans =mid 
                low=mid+1
            else:
                high = mid-1
        return ans