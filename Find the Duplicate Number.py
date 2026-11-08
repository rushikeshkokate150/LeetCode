class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        hash = [0]*(n)
        
        for  i in range(n):
            hash[nums[i]]+=1
        
        for i in range(n):
            if hash[i] > 1:
                return i
        