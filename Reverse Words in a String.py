class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arr = arr[::-1]
        ans = ""
        j  = 0
        while j < len(arr) and arr[j] == "":
            j+=1 
        
        if j < len(arr) and arr[j] != "":
            ans+=arr[j]

        for i in arr[j+1:]:
            if i == "":
                continue
            ans += " "
            ans += i
        return ans

