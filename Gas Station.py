    # Brute Force Approach
        # n = len(gas)
        
        # def check(i):
        #     capacity = 0 + gas[i] - cost[i]
        #     last = i
        #     i = (i+1) % n
        #     while i != last:
        #         capacity = (capacity+gas[i])-cost[i]
        #         if  capacity < 0:
        #             return False
        #         i = (i+1) % n
        #     return True



        # for i in range(n):
        #     if gas[i] - cost[i] < 0:
        #         continue
        #     else:
        #         if check(i):
        #             return i
        # return -1



class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        start = 0
        total = 0
        tank = 0

        for i in range(n):
            dif = gas[i] - cost[i]

            total += dif
            tank += dif

            if tank < 0:
                start = i+1
                tank = 0
        
        return start if total >= 0 else -1

