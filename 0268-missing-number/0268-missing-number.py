class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        total_sum = length*(length+1)//2
        actual_sum = sum(nums)
        missing_number = total_sum - actual_sum
        return missing_number