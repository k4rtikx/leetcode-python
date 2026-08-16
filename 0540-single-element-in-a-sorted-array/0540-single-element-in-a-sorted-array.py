class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low + ((high-low)//2)
            if len(nums)==1 :
                return nums[0]
            if low==0 and nums[low] !=nums[low+1]:
                return nums[low]

            elif high ==len(nums)-1 and nums[high] !=nums[high -1]:
                return nums[high]

            # now low become 1 and high become piche se -2  (binary search implementation)
            else:
                if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1] :
                    return nums[mid]
                
                # mid=even and next element same    or   mid = odd and previous element is same then move front 
                elif  mid %2==0 and nums[mid] == nums[mid+1]  or mid %2==1 and nums[mid] == nums[mid-1]:
                    low=mid+1
                # or move back 
                else: 
                    high=mid-1