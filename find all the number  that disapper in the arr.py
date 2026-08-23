class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        n =len(nums)

        ans = []
        prev = lower

        for i in nums:
            if i < lower or i > upper:
                continue

            if i > prev:
                ans.append([prev,i-1])

            prev = max(prev,i+1)
        if prev <= upper:
            ans.append([prev,upper])
    

        return ans
            
            