class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        left = len(nums) - k
        right = len(nums) - 1

        for i in range(k // 2):
            nums[left + i], nums[right - i] = nums[right - i], nums[left + i]
        
        m=len(nums)-k
        for i in range (m//2):
            nums[i],nums[m-1-i]=nums [m-1-i],nums[i]
        
        
        for i in range (len(nums)//2):
            nums[i],nums[len(nums)-1-i]= nums[len(nums)-1-i], nums[i]

        return nums
