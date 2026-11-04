class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def isidentical(node1, node2):
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            lf = isidentical(node1.left, node2.left)
            rt = isidentical(node1.right, node2.right)

            return lf and rt

        def preorder(node):
            if node is None:
                return False

            if node.val == subRoot.val:
                if isidentical(node, subRoot):
                    return True

            lf = preorder(node.left)
            if lf:
                return True

            rt = preorder(node.right)
            if rt:
                return True

            return False

        if subRoot is None:
            return True

        if root is None:
            return False

        return preorder(root)