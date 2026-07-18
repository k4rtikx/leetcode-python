class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1 # =first_arr_last
        j=n-1 #second_arr_last
        k=len(nums1) -1 #=zero_last
        while i>=0 and j>=0:#nums1!=0 or nums2!=0:
            if nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                j-=1
            else:
                if nums2[j]<=nums1[i]:
                    nums1[k]=nums1[i]
                i-=1
            k-=1 # k is comman so we have taken outside 
        # Copy remaining elements from nums2 (if any)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1