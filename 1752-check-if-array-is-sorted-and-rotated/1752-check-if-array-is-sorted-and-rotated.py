# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         final=True
#         for i in range (len(nums)-1):
#             if nums[i]>nums[(i+1)% n]:
#                 final=False
#                 break
#         return final
#         #print(final)

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

            if count > 1:
                return False

        return True