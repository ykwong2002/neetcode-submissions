class Solution:
    def rob(self, nums: List[int]) -> int:
        pp, p = 0, 0

        for num in nums:
            temp = max(num + pp, p)
            pp = p
            p = temp
        
        return temp
"""
Goal: return max sum of nums where i cannot touch adjacent integers
- dynamic programming
- the current amount i can have robbed at i = max(curr + i - 2, i - 1)
"""