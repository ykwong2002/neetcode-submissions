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
                return 0, True # If no node, height = 0, balanced = True
            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)

            curr_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            return max(left_height, right_height) + 1, curr_balanced
        
        return dfs(root)[1]