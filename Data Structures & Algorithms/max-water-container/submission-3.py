class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            max_area = max(curr, max_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

            
"""
0   1   2   3   4   5   6   7   8   9   10  11  12  13
1   7   2   5   12  3   500 500 7   8   4   7   3   6
    l                       r
curr = 7 * 6 = 42
max_area = 72

3   3   4   2   2
Goal: Calculate the maximum area formed by the numbers in heights
0   1   2   3   4   5   6   7
1   7   2   5   4   7   3   6
    l                       r    
area = min(l, r) * (l - r)
curr = 28
max_area = 36
"""