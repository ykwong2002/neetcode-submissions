# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left) # height of left
            right = dfs(root.right) # height of right
            res = max(res, left + right) # diameter = left span + right span
            return 1 + max(left, right) # return the new height
        
        dfs(root)
        return res
            
        