# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        # DFS on child nodes
        self.invertTree(root.left) 
        self.invertTree(root.right)
        # Swap left and right children after they have been DFSed
        root.left, root.right = root.right, root.left
            
        return root
        