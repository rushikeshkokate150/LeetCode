from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        q = deque()
        q.append(root)
        str1 = ""
        while q:
            n = len(q)
            for i in q:
                if i == None:
                    str1+='None'
                    str1 += ' '
                    continue
                str1 += str(i.val)
                str1+= ' '
            for i in range(n):
                node = q.popleft()
                # print(node)
                if node == None:
                    continue
                q.append(node.left)
                q.append(node.right)
        # print(str1)
        return str1


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        arr = data.split(" ")
        # arr.pop()
        # print(arr)
        
        root = TreeNode(arr[0])
        i = 1
        node = root
        q = deque()
        q.append(node)
        while q:
            n = len(q)
            for r in range(n):
                j = q.popleft()
                if j == None:
                    continue
                else:
                    j.left = TreeNode(int(arr[i])) if arr[i] != 'None' and arr[i] != '' else None
                    q.append(j.left)
                    i += 1
                    j.right = TreeNode(int(arr[i])) if arr[i] != 'None' and arr[i] != '' else None
                    q.append(j.right)
                    i += 1

        return root
