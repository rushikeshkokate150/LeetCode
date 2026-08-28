class Solution:
    def reverseBits(self, n: int) -> int:
        a = f"{n:032b}"
        a = a[::-1]
        number = int(a, 2)
        return number