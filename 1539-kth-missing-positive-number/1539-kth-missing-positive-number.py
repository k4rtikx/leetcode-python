class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        low=0
        high=len(a)-1
        while low<=high:
            mid=(low+high)//2
            missing =a[mid]-(mid+1)
            if missing<k:
                low=mid+1
            else:
                high=mid-1
        # derivation see in vs code in Kth Missing Positive Number
        return low+k