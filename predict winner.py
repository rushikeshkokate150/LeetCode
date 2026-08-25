class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def f(i, j):

            # Only one number left
            if i == j:
                return nums[i]

            # Choose left
            left = nums[i] - f(i + 1, j)

            # Choose right
            right = nums[j] - f(i, j - 1)

            return max(left, right)

        return f(0, len(nums) - 1) >= 0