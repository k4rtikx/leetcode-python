class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        s = set(nums)
        mn = min(nums)
        mx = max(nums)
        for i in range(mn, mx + 1):
            if i not in s:
                ans.append(i)
        return ans