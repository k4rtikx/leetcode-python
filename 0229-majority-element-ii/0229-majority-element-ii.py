class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_1 = 0
        count_2 = 0
        element_1 = 0
        element_2 = 0

        for i in range(len(nums)):
            if count_1 == 0 and element_2 !=nums[i]:
                count_1 += 1
                element_1=nums[i]

            elif count_2 ==0 and element_1 !=nums[i]:
                count_2 += 1
                element_2=nums[i]
    
            elif element_1 == nums[i]:
                count_1 += 1

            elif element_2 == nums[i]:
                count_2 += 1
    
            else:
                count_1-=1
                count_2-=1
        #print(element_1,element_2)
        # manual check 
        count_1=0
        count_2=0
        ans=[]
        for i in range (len(nums)):
            if element_1==nums[i]:
                count_1+=1
            elif element_2==nums[i]:
                count_2+=1
        if count_1 >= len(nums) // 3+1:
            ans.append(element_1)

        if count_2 >= len(nums) // 3+1:
            ans.append(element_2)
        #print(ans)
        return ans