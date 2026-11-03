"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def h(node):
            if node == None:
                return 0
            
            maxi = 0
            for i in node.children:
                ht = h(i)
                maxi = max(maxi,ht)
            
            return maxi+1
        
        return h(root)
