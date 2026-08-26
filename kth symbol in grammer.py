class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def f(n, k):

            if n == 1:
                return 0

            half = 2 ** (n - 2)

            if k <= half:
                return f(n - 1, k)
            else:
                return 1 - f(n - 1, k - half)

        return f(n, k)