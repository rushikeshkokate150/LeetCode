class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        n = len(number)
        for i in range(n):
            if number[i] == digit:
                st = number[:i]+number[i+1:]
                ans = max(ans , int(st))
        return str(ans)
