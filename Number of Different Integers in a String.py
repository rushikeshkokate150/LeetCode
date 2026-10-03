class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        n = len(word)
        s = ""

        for i in range(n):
            if word[i] >= 'a' and word[i] <= 'z':
                s += " "
                continue
            else:
                s += word[i]
        arr = set(map(int, s.split()))
        
        return len(arr)

            
