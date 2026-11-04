# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False

"""
Goal: check if all values of trees p and q are the same (also in same pos i.e. .left and .right)
base case:
    - if no value at p and no value at q, return True
recrusive step:
    - if p and q both have values and are equal, recursively check if p.left == q.left and p.right == q.right

else:
    - return False

"""