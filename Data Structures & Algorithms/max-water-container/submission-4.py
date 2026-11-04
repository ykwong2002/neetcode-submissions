class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maximum = max(maximum, area)
            if heights[l] > heights[r]: # keep l, move r
                r -= 1
            else:
                l += 1
        
        return maximum
"""
Goal: find max area of container:
- area: min(left bar, right bar) * (right bar - left bar)
- initialise maximum to 0
- two pointers from extreme ends
- calculate area, update the maximum
- keep the bigger bar --> higher chance of returning a larger area

0   1   2   3   4   5   6   7
1   7   2   5   4   7   3   6
    l
                        r
max = 36
"""