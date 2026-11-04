# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        arr = []
        def inorder(node):
            nonlocal ans
            if node == None:
                return
            inorder(node.left)
            if len(arr) != 0:
                ans = min(ans,abs(arr[-1]-node.val))
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        
        return  ans