"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        d = {}
        def dfs(node):
            if node in d:
                return d[node]
            copy = Node(node.val)
            d[node] = copy
            # copy the neighbours
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)
"""
Goal: Create a deep copy of the graph. 
- there may be cycles, so need to track what we have already created
- if input node is null, return null
- initialise dictionary of Node (old) : Node (copy)
- perform dfs on the initial node:
    - if node already in dictionary (created), return the copied node
    - else, create a copy and store it in the dictionary
    - for each neighbour of the node, add it to the copy's neighbours (use recursive dfs to check if it has been created)
"""