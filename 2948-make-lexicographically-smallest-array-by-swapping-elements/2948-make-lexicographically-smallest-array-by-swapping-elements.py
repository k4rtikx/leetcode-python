class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        # Keep value + original index
        arr = [(nums[i], i) for i in range(len(nums))]

        # Sort by value
        arr.sort()

        result = nums[:]

        i = 0

        while i < len(arr):

            # Find one group
            j = i

            while j + 1 < len(arr) and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Extract values and original indices
            values = []
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            # Sort original indices
            indices.sort()

            # Put sorted values into sorted original indices
            for k in range(len(indices)):
                result[indices[k]] = values[k]

            # Move to next group
            i = j + 1

        return result