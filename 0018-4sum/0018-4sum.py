class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:     
        i=0
        nums.sort()
        ans=[]

        # [-4, -1, -1, 0, 1, 2]
        while i<len(nums)-3:
            j=i+1
                    
            while j<len(nums)-2:
                k=j+1
                l=len(nums)-1
                while k<l:
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total==target and i<j<k<l:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        print(nums[i],nums[j],nums[k],nums[l])
                        while k < l and nums[l] ==nums[l-1]:
                            l-=1
                        l-=1
                        while k < l and nums[k] ==nums[k+1]:
                            k+=1
                        k+=1 

                    elif total>target and i<j<k<l:
                        l-=1

                    elif total <target and i<j<k<l:
                        k+=1 
                while j<len(nums)-2 and nums[j] ==nums[j+1]:
                    j+=1
                j+=1

            while i<len(nums)-3 and nums[i] ==nums[i+1]:
                i+=1
            i+=1
        return ans