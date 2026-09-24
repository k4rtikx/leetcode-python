class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        for i in range(len(a)):
            summ=0
            num=a[i]
            while num >0:
                d=num%10
                summ+=d
                num//=10
            if summ==i:
                return i
                break
        else:
            return -1