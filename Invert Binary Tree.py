# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root == None:
            return root 

        def invertfunction(node):
            if node == None:
                return 
            left = invertfunction(node.left)
            right = invertfunction(node.right)
            node.left,node.right = node.right,node.left
        
        invertfunction(root)
        return root
