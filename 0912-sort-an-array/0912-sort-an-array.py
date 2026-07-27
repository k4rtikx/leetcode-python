class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide( nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=divide(nums[:mid])
            right= divide(nums[mid:])
            return merge(left,right)

        def merge(left,right):
            i=j=0 
            total=[]
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    total.append(left[i])
                    i+=1
                else:
                    total.append(right[j])
                    j+=1
            while i<len(left):
                total.append(left[i])
                i+=1
            while j<len(right):
                    total.append(right[j])
                    j+=1
            return total

        output=divide(nums)
        return output

        