class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0]*m for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][0] = 1 if matrix[i][0] == 1 else 0
            ans += dp[i][0]
        # print(ans)

        for j in range(1,m):
            dp[0][j] = 1 if matrix[0][j] == 1 else 0
            ans += dp[0][j]
        # print(dp)
        # print(ans)
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    continue
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                ans += dp[i][j]
        # print(dp)
        return ans
        
        