class Solution:
    def arrayRankTransform(self, arr):
        unique = sorted(set(arr))

        rank = {}

        for i in range(len(unique)):
            rank[unique[i]] = i + 1

        ans = []

        for num in arr:
            ans.append(rank[num])

        return ans