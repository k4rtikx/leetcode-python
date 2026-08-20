class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high = max(nums)
        ans=-1
        while low <=high:
            total=0
            mid=low + ((high-low)//2)
            for j in nums :
                total+=(j+mid-1)//mid
            if total <=threshold:
                ans=mid
                high = mid-1
            else:
                low = mid+1
        return ans