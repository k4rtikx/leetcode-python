class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ori_student= k
        low = max(nums)
        high = sum (nums)
        while low <=high :
            mid=low + ((high-low)//2)
            student=1
            allocation=nums[0]
            for j in range (1, len(nums)):
                if allocation + nums[j] <= mid :   
                    allocation+=nums[j]
                else:
                    student+=1
                    allocation=nums[j]
            if student <= ori_student:
                answer=mid
                high = mid-1
            else:
                low = mid+1
        return answer
                