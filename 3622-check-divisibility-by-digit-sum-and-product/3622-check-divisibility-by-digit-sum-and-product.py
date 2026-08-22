class Solution:
    def checkDivisibility(self, n: int) -> bool:
        copy=n
        summ=0
        multi=1
        while copy >0:
            b= copy % 10
            summ+=b
            multi*=b
            copy = copy // 10
        if n % (summ+ multi) ==0:
            return True
        else:
            return False
            