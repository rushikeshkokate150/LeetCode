class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0

        visited = [[0]*m for _ in range(n)]

        def dfs(i,j):
            nonlocal cnt
            cnt += 1
            visited[i][j] = 1
            
            for x,y in ((0,1),(1,0),(-1,0),(0,-1)):
                X = x+i
                Y = y+j

                if X<0 or Y<0 or X>=n or Y >= m or grid[X][Y] == 0 or visited[X][Y]==1:
                    continue
                dfs(X,Y)

        ans = 0


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    cnt = 0
                    dfs(i,j)
                    ans = max(ans,cnt)
        
        return ans
