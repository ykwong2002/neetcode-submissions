class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Pair of (index, height)

        for i, h in enumerate(heights):
            start = i
            # While height of top of stack > height of current height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

"""
Goal: return area of largest rectangle formed among bars
- area = height (min of stack) x width (len of stack)
7   1   
"""