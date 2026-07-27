class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        from array import array 
        
        n=len(nums)
        lar = float("-inf")
        smal = float("-inf")
        for i in range (n):
            if nums[i]>lar:
                smal=lar
                lar=nums[i]
            elif nums[i]>smal :
                smal=nums[i]
        return (lar-1)*(smal-1)
