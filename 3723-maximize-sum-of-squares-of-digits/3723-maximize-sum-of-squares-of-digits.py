class Solution:
    def maxSumOfSquares(self, num: int, summ: int) -> str:
        if summ > 9 * num:
            return ""  
        string = ""

        total_nine = summ // 9
        string += "9" * total_nine

        remaining = summ % 9

        if remaining > 0:
            string += str(remaining)

        zeros = num - len(string)
        string += "0" * zeros

        return string