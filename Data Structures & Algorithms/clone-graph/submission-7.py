"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d = {}

        def dfs(node):
            if node in d:
                return d[node]
            copy = Node(node.val)
            d[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)
"""
Goal: return deep copy of a graph starting from the starting node
- DFS
- start from node
- be careful of cycles --> may end up recreating the same node again if i do not track
- use dictionary to track old node to new node (if exists in dictionary, return the new node)
"""