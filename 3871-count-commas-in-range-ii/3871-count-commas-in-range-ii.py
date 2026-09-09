class Solution:
    def countCommas(self, n: int) -> int:
        p=1000
        ans=0
        while p<=n:
            ans+=n-p+1 # n-999 then n-999999
            p*=1000
        return ans
