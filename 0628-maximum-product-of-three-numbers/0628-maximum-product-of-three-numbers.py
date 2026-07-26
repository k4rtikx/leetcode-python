class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product_1=1
        product_2=1
        for i in range(3):
            product_1*=nums[len(nums)-1-i]
            if i<2:
                product_2*=nums[i]
        product_2*=nums[len(nums)-1]
        # INSTEAD OF THAT WE CAN DIRECTLY WRITE THIS 
        # product_1 = a[-1] * a[-2] * a[-3]
        # product_2 = a[0] * a[1] * a[-1]
        if product_1 > product_2:
            #print(f"max product of 3 num is {product_1}")
            return product_1
        else:
            #print(f"max product of 3 num is {product_2}")
            return product_2