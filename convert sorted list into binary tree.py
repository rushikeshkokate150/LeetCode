# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        # print(arr)
        n = len(nums)

        def createBST(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = createBST(left, mid - 1)
            root.right = createBST(mid + 1, right)

            return root
        
        return createBST(0, n - 1)