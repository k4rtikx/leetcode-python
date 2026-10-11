class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length = len(nums)
        store=0
        for element in range(1,length +1):
            if length % element == 0:
                store += nums[element-1]*nums[element-1]
        return store