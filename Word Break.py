class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dict1 = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        i = 0
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] in dict1 and dp[j] == True:
                    dp[i] = True
        
        return dp[-1]