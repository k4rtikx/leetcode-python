class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #Lower bound
        first=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low + ((high-low)//2)
            if nums[mid]  >= target:
                first=mid
                high=mid-1 # go left
            elif nums[mid]<target:
                low=mid+1
        # first not found
        if first==-1 or target!=nums[first]:
            return [-1,-1]
        # upper bound
        last=len(nums)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low + ((high-low)//2)
            if nums[mid]  > target:
                last=mid
                high=mid-1 
            elif nums[mid]<=target:
                low=mid+1
        return [first , last-1]
