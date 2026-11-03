class Solution:
    def minMoves(self, nums: List[int]) -> int:
        b = max(nums)
        total = sum(b - x for x in nums)
        return total