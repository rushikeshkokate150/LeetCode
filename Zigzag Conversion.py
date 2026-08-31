class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = []
        j = 0
        i = 0

        while i < len(s):
            temp = []
            while j < numRows and i < len(s):
                temp.append(s[i])
                i+=1
                j+=1
            while len(temp) < numRows:
                temp.append(0)
            arr.append(temp)
            j=numRows-2
            while j > 0 and i < len(s):
                temp = [0]*numRows
                temp[j] = s[i]
                arr.append(temp)
                j-=1
                i+=1
        

        n = len(arr)
        m = len(arr[0])

        ans = ""
        for j in range(m):
            for i in range(n):
                if arr[i][j] != 0:
                    ans+=arr[i][j]
        return ans 

                

                


            