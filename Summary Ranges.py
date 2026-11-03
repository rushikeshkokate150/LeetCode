class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n = len(nums)

        if n == 0:
            return []

        ans = []
        start = nums[0]
        i = nums[0]

        for j in nums:
            if j != i:
                if start == i - 1:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(i - 1))

                start = j
                i = j

            i += 1

        if start == nums[-1]:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(nums[-1]))

        return ans