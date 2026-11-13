class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        ans = 0

        def check(k):
            totalhr = 0

            for pile in piles:
                totalhr += math.ceil(pile / k)

            return totalhr <= h

        while l <= r:
            mid = (l+r) // 2
            
            val = check(mid)
            if val:
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans