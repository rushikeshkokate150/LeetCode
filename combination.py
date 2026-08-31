class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def f(ind,arr):
            if len(arr) == k:
                # print(arr)
                ans.append(arr[:])
                return
            if ind > n:
                return
            arr.append(ind)
            f(ind+1,arr)
            arr.pop()
            f(ind+1,arr)
        
        arr = []
        f(1,arr)
        return ans
