class Solution:
    def isPalindromic(self, s: str) -> bool:
        def palidrom(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
            
        ans = ""
        for i  in s:
            val = format(ord(i),'08b')
            ans += val

        return palidrom(ans)

        