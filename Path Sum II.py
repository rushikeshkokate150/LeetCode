# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def path(temp,arr):
            nonlocal ans
            # arr.append(temp.val)
            if temp == None:
                return 

            if temp.left == None and temp.right == None:
                arr.append(temp.val)
                # print(arr)
                if sum(arr) == targetSum:
                    # print(arr)
                    ans.append(arr[:])
                arr.pop()
                return
            arr.append(temp.val)
            leftn = path(temp.left,arr)
            rightn = path(temp.right,arr)
            arr.pop()
        
        temp = root
        path(temp,[])
        return ans

