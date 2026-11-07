# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        sum1 = 0
        def fuction(node,str1):
            nonlocal sum1
            str1+=str(node.val)
            print(str1)
            if node.left == None and node.right == None:
                sum1 += int(str1)
                return
            if node == None:
                return
            if node.left != None:
                # print(str1,"before")
                lt = fuction(node.left,str1)
                # print(str1,"after")
            if node.right != None:
                rt = fuction(node.right,str1)
        
        fuction(root,'')
        return sum1
