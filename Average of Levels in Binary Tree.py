from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            # print(q)
            # print()
            sum1 = 0
            for i in range(n):
                node = q.popleft()
                sum1+=node.val
                if node.left:
                    q.append(node.left)  
                if node.right:
                    q.append(node.right)  
            ans.append(sum1/n)
        
        return ans

