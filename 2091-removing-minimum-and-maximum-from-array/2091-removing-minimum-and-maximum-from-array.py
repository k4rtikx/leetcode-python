class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn=float("+inf")
        maxx=float("-inf")
        small=high=0
        for i in range (len(nums)):
            if len(nums)==1:
                return 1
            if nums[i]<= minn:
                minn=nums[i]
                small=i
            if nums[i]>= maxx:
                maxx=nums[i]
                high=i
        # i want value how may it is removed so 
            option1 = max(small, high) + 1  # from front 3 element 
            option2 = len(nums) - min(small, high) # from back  8- 1 = 7 element removed 
            option3 = min(small, high) + 1 + len(nums) - max(small, high) # from front and back 1 +1+8 -5 = 5
        return min(option1,option2,option3)