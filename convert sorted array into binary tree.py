class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def createBST(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = createBST(left, mid - 1)
            root.right = createBST(mid + 1, right)

            return root

        return createBST(0, len(nums) - 1)