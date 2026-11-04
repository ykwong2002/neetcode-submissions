class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def helper(arr):
            pp, p = 0, 0
            for n in arr:
                temp = max(n + pp, p)
                pp = p
                p = temp
            return p
        
        return max(helper(nums[1:]), helper(nums[:-1]))
"""
Goal: return max sum of nums such that i do not add any adjacent integers
- houses are in a circle: cannot rob both first and last houses at the same time
- HR1 but exclude 1st, then exclude last
"""