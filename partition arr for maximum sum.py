class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        def f(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            leng = 0
            maxans = -1
            maxi = -1
            for j in range(i,min(n,i+k)):
                leng += 1
                maxi = max(maxi,arr[j])
                sum1 = (leng*maxi) + f(j+1)
                maxans = max(maxans,sum1)
            
            dp[i] = maxans
            return dp[i]
        
        n = len(arr)
        dp = [-1]*n

        return f(0) 