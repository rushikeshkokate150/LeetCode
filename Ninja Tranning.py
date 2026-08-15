n = 3
dp = [[-1]*4 for _ in range(n)]

task = [[18,11,19],[4,13,7],[1,8,13]]

def traning(ind,last):
    if ind == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi,task[0][i])
        return maxi
    
    if dp[ind][last] != -1:
        return dp[ind][last]
    maxi1 = 0
    for i in range(3):
        if i != last:
            point = task[ind][i] + traning(ind-1,i)
            maxi1 = max(maxi1,point)
    
    dp[ind][last] = maxi1
    return dp[ind][last]

print(traning(2,3))