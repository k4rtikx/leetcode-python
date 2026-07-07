class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = list(str(n))
        summ = 0
        without_zero = '0'
        for i in range(len(n)):
            if n[i] == '0':
                continue
            else:
                summ += int(n[i])
                without_zero += n[i]
        b = int(without_zero) * summ
        return b