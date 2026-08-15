class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        arr = [0]
        arr.extend(cuts)
        arr.append(n)
        arr.sort()
        m = len(cuts) 

        dp = [[-1]*(m+1) for _ in range(m+1)]

        # print(arr)

        def cuttt(i,j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            mini = 100000000
            for ind in range(i,j+1):
                cost = arr[j+1]-arr[i-1]+cuttt(i,ind-1)+cuttt(ind+1,j)
                mini = min(mini,cost)
            dp[i][j] = mini
            return dp[i][j]
        
        return cuttt(1,m)
