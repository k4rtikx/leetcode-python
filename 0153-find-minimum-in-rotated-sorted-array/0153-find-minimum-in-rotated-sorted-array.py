class Solution:
    def findMin(self, nums: List[int]) -> int:
        low =0
        high = len(nums)-1
        ans=inf = float('inf')
        while low <=high:
            mid=low + ((high-low)//2)
            # left side sorted 
            if nums[low] <=nums[mid]:
                ans= min (nums[low], ans)
                low=mid+1
            elif nums[mid] <=nums[high]:
                ans= min(nums[mid] , ans)
                high=mid-1
        return ans
                