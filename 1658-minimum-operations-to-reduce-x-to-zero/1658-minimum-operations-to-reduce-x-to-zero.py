class Solution:
    def minOperations(self, a: list[int], x: int) -> int:
        total_add=0
        for i in range (len(a)):
            total_add += a[i]
        #print(total_add)
        k=total_add-x
        if k < 0:
            return -1
        if k == 0:
            return len(a)
        # longest continuous subarray
        summ=0
        max_len=0
        i=j=0
        while j<len(a):
            summ+=a[j]
            while summ>k:
                summ-=a[i]
                i+=1
            if summ==k:
                max_len=max(max_len, j-i+1)
            j+=1
        # print(max_len)
        if max_len == 0:
            final_answer = -1
        else:
            final_answer = len(a) - max_len
        return final_answer
