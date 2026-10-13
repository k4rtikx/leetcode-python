class Solution:
    def maxAlternatingSum(self, a: List[int]) -> int:
        for i in range(len(a)):
            a[i] = a[i] ** 2
        a.sort()
        b=len(a)
        score=0
        for i in range (b//2):
            score+=a[b-1-i] -a[i]
        if b % 2 != 0:
            score+=a[b // 2]
        return score