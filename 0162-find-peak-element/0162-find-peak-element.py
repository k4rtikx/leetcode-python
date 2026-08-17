class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=1
        high=len(nums)-2

        if len(nums)==1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        #binary search
        else:
            while low <=high:
                if nums[low-1] > nums[low]:
                    return low-1
                elif nums[high+1] > nums[high]:
                    return high+1
                
                else:
                    mid=low + ((high-low)//2)
                    if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1] :
                        return mid
                    elif nums[mid] < nums[mid+1]:
                        low=mid+1
                    else :
                        if nums[mid] > nums[mid+1]:
                            high =mid-1
        return -1