class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0] * n
        
        # Exception: If less than 2 blocks, cannot hold water
        if n < 3:
            return 0
        
        prefix = [0] * n
        max_prefix = 0
        # Build prefix array (greatest before)
        for i in range(1, n):
            max_prefix = max(max_prefix, height[i - 1])
            prefix[i] = max(prefix[i], max_prefix)

        suffix = [0] * n
        max_suffix = 0
        # Build suffix array (greatest after)
        for i in range(n - 2, -1, -1):
            max_suffix = max(max_suffix, height[i + 1])
            suffix[i] = max(suffix[i], max_suffix)
        
        for i in range(1, n):
            water[i] = max(min(prefix[i], suffix[i]) - height[i], 0)
        
        return sum(water)
        
"""
Goal: find max area BETWEEN bars

0   1   2   3   4   5   6   7   8   9   10  11
0   2   0   3   1   0   1   3   2   1

0   0   2   2   3   3   3   3   3   3              prefix
3   3   3   3   3   3   3   2   1   0              suffix
    c
0   0   2   0   0   0   0   0   0   0               water

units of water a block can store = min(heights[l], height[r]) - height[curr]
if ^ is negative, become 0
total = 0

"""