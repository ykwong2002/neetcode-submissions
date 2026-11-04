class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # prefix pass
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        
        # postfix pass
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
"""
Goal: return a list containing products of the whole array except iteself
- intuition would be to find total product and divide over each answer
    - may face zero division error
- instead, use prefix and postfix calculation to carry over
    - multiplication is always done wrt the original array
        1   2   4   6
e.g
prefix:
res     1   1   1   1
res     1   1   1   1
res     1   1   2   8
postfix:
res     1   1   2   8
res     1   1   12   8

"""