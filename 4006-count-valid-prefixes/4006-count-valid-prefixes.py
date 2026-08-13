class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count_0 = 0
        count_1 = 0
        valid_prefixes = 0

        for char in s:
            if char == '0':
                count_0 += 1
            else:
                count_1 += 1

            if abs(count_0 - count_1) <= 1:
                valid_prefixes += 1
        
        return valid_prefixes