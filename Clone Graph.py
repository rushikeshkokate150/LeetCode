
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        hashmap = {}

        def dfs(curr):
            if curr in hashmap:
                return hashmap[curr]

            clone = Node(curr.val)
            hashmap[curr] = clone

            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)
