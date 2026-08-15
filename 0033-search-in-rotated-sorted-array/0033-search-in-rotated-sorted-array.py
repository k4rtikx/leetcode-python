class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1
        while low <=high:
            mid=low + ((high-low)//2)
            
            if nums[mid]==target :
                return mid
            # find left side is sorted or not 
            elif nums[mid] >= nums[low] :
                if nums[low] <= target and nums[mid] >=target:
                    high=mid-1
                else:
                    low=mid+1
            # find right is  sorted or not 
            else:
                if nums[mid] <= target and nums[high] >=target:
                    low=mid+1
                else:
                    high =mid-1
        return -1