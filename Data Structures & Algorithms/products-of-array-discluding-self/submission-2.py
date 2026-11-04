class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Prefix update loop
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        
        # Postfix update loop
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
"""
Goal: return an array where each index is the product of all other indexes (excluding itself)
- Initialise a res array of all [1, 1, 1, ...]
- initialise a prefix (contains product of all prev indexes)
    - update each index along the way
    - update the prefix

- initialise a postfix (contains product of all post indexes)
    - update each index backwards along the way
    - update the postfix

nums =  [1, 2, 4, 6]
res =   [1, 1, 2, 8]
postfix = 1
"""