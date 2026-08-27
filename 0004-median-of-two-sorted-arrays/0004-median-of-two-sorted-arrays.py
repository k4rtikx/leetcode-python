class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # optimal apporach 
        if len (nums1) > len(nums2):
            temp=nums1
            nums1=nums2
            nums2=temp
        low = 0 
        high =len(nums1)
        while low <=high :
            mid1=low + ((high-low)//2) # 2 
            mid2= (((len(nums2)+len(nums1))+1)//2 )-mid1#  total 10 /2 = 5 -mid1 so it become 3 
            l1=float("-inf")
            l2=float("-inf")
            r1=float("inf")
            r2=float("inf")
            if mid1-1>=0:
                l1=nums1[mid1-1]
            if mid2-1>=0:
                l2=nums2[mid2-1]
            if mid1 < len(nums1):
                r1 = nums1[mid1]
            if mid2 < len(nums2):
                r2 = nums2[mid2]

            # cross check 
            if l1 <= r2 and l2 <=r1:
                if ((len(nums1)+ len(nums2)) %2 )==0 :
                    even= (max(l1,l2) + min(r1,r2))/2
                    return even
                else :
                    odd = max(l1, l2)
                    return odd
                break

            elif l1 >r2:
                high=mid1-1
            else:
                low=mid1+1
