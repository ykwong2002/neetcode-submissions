class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def helper(arr):
            pp, p = 0, 0

            for n in arr:
                temp = max(pp + n, p)
                pp = p
                p = temp
            return p
        
        return max(helper(nums[1:]), helper(nums[:-1]))
"""
Goal: similar to HR1, goal is to return max i can rob without robbing adjacent houses
- NOW, extra constraint: first and last houses are next to each other
- can reuse the answer from HR1 (returns max that can be robbed)
    - perform on 2 subarrays (exclude first elem, exclude last elem)
    - since first and last elem cannot be robbed on the same night
"""