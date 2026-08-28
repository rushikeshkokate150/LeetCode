class Solution:
    def hammingWeight(self, n: int) -> int:
        a = f"{n:b}"
        cnt = 0
        for i in a:
            if i == '1':
                cnt+=1
        return cnt 