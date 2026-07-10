class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        #print(pos)
        #print(neg)
        c=min(len(pos),len(neg))
        d=max(len(pos),len(neg))
        #print(c)
        for i in range(c):
            nums[i*2]=pos[i]
            nums[i*2+1]=neg[i]
        #print(nums)
        for i in range (d,len(nums)):
            if len(pos)>len(neg):
                nums[i]=pos[c]
                c+=1
            elif len(pos)<len(neg):
                nums[i]=neg[c]
                c+=1
        #print(nums)
        return nums