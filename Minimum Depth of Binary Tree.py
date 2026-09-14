class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:  
        if not root:
            return 0

        temp = root
        ans = 1e9  

        def height(temp,cnt):
            nonlocal ans
            if temp == None:
                return 
            if temp.left == None and temp.right == None:
                ans = min(ans,cnt)

            leftN = height(temp.left,cnt+1)
            rightN = height(temp.right,cnt+1)
        
        height(temp,1)
        return ans
