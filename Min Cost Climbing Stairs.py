from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @lru_cache(None)
        def func(ind):
            if ind >= len(cost):
                return 0
            first = cost[ind] + func(ind+1)
            second = cost[ind] + func(ind+2)
            # print(first,second)

            return min(first,second)
        a = func(0)
        b = func(1)
        
        return min(a,b)