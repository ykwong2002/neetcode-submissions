# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [0, True]
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Current balance
            balance = abs(left[0] - right[0]) <= 1 and left[1] and right[1]
            return [max(left[0], right[0]) + 1, balance]
        
        return dfs(root)[1]
"""
Goal: check whether every node in the tree is balanced (left and right max depth differs by 1 or 0) AVL?
- perform dfs on the node:
    - check height of left subtree 
    - check height of right subtree
    - check if it is balanced (meaning abs(left - right) <= 1)
    - return the height of the tree and whether or not it is balanced to the parent
"""