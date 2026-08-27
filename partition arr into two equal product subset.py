class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        product = 1
        for i in nums:
            product *= i
        
        if product/target != target:
            return False
        
        def f(ind,prd):
            if ind == n:
                if prd == target:
                    return True
                else:
                    return False
                
            nottake = f(ind+1,prd)
            take = f(ind+1,prd*nums[ind])
            return nottake or take 
        
        qq = f(0,1)

        return qq