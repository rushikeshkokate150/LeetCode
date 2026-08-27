class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return 'a'
        
        word = "a"
        i =len(word)
        # print("starting",i)
        while i < k: 
            for ch in word:
                if ch == 'z':
                    word+='a'
                    continue
                next_ch = chr(ord(ch) + 1)
                word+=next_ch
            i = len(word)
            # print(word)
            # print(i)
        
        return word[k-1]

