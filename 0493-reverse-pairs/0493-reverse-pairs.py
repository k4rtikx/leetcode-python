class Solution:
    def reversePairs(self, nums):
        self.count = 0

        def divide(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = divide(nums[:mid])
            right = divide(nums[mid:])

            return merge(left, right)

        def merge(left, right):
            # -------- Count Reverse Pairs --------
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    self.count += (len(left) - i)
                    j += 1
                else:
                    i += 1

            # -------- Normal Merge --------
            i = j = 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        divide(nums)
        return self.count