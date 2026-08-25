class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        for i in range (1, 101+1):
            if k*i in nums:
                continue 
            else :
                return k*i