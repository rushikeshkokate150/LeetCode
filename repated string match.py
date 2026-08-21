class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        string1 = ""
        cnt = 0
        while len(string1) < len(b):
            string1 += a
            cnt += 1
        
        if b in string1:
            return cnt
        
        
        string1 += a
        cnt += 1
        
        if b not in string1:
            return -1
        return cnt
