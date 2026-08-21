class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prevstring = "1"
        newstring = ""

        for i in range(2,n+1):
            cnt = 0
            prev = ""
            for j in range(len(prevstring)):
                if prev == "":
                    prev = prevstring[j]
                    cnt += 1
                elif prevstring[j] == prev:
                    cnt += 1
                else:
                    newstring += str(cnt)
                    newstring += prev
                    cnt = 1
                    prev = prevstring[j]
            
            if cnt != 0 and prev != "":
                newstring += str(cnt)
                newstring += prev
            prevstring = newstring
            newstring = ""
        
        return prevstring
