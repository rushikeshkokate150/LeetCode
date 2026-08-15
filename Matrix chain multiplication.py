arr = [10,20,30,40,50]
n = len(arr)

dp = [[-1]*n  for _ in range(n)]
# def mult(i,j):
#     if i == j:
#         return 0
#     if dp[i][j] != -1:
#         return dp[i][j]
#     mini = 100000000
#     for k in range(i,j):
#         step  = (arr[i-1]*arr[k]*arr[j]) + mult(i,k)+mult(k+1,j)
#         mini = min(mini,step)
#     dp[i][j] = mini
#     return dp[i][j]

# print(mult(1,4))

# now using tabultaion
for i in range(n):
    dp[i][i] = 0

for  i in range(n-1,-1,-1):
    for j in range(i+1,n):
        mini = 1e9
        for  k in range(i,j):
            step  = (arr[i-1]*arr[k]*arr[j]) + dp[i][k]+dp[k+1][j]
            mini = min(mini,step)
        dp[i][j] = mini
print(dp[1][n-1])
        
        