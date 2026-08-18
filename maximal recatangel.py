def largestRectangleArea(heights):
    n = len(heights)
    if len(heights) == 0:
        return 0
    if len(heights) == 1:
        return heights[-1] 
        
    ans = 0
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            val = stack.pop()
            if len(stack) == 0:
                prev = -1
            else:
                prev = stack[-1]
            res = heights[val]*(i-prev-1)
            ans = max(ans,res)
        stack.append(i)
        
    i = n 
    while stack:
        val =stack.pop()
        if len(stack) == 0:
            prev = -1
        else:
            prev = stack[-1]
        res = heights[val]*(i-prev-1)
        ans = max(ans,res)
    return ans
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxans = -1
        row = len(matrix)
        col = len(matrix[0])
        arr = [0] * col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    arr[j] += 1
                else:
                    arr[j] = 0
                
            val = largestRectangleArea(arr)
            maxans = max(maxans,val)
        return maxans