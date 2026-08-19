class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=-1
        while low<=high:
            mid=low + ((high-low)//2)
            # calculation 
            total_hour=0
            for pile in piles:
                total_hour +=(pile + mid - 1) // mid
            if total_hour <= h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
