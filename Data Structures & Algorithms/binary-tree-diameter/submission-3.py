# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        
        def dfs(node):
            nonlocal result
            """
            take in a node, return the max depth of the node
            """
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # Update the result
            result = max(result, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return result
            
"""
Goal: return diameter of binary tree: difference between leftest and rightest
- for each node, calculate diameter (left subtree + right subtree)
    - diameter = max of left subtree + max of right subtree
- update the global result (max of result and diameter)
- return the height to the parent
"""