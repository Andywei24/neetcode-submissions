"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            cpy = Node(node.val)
            oldToNew[node] = cpy
            for nei in node.neighbors:
                cpy.neighbors.append(dfs(nei))
            return cpy
        return dfs(node) if node else None


            