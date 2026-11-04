class Solution:
    def trap(self, height: List[int]) -> int:
        maximum = 0

        # find max_left
        max_left = [0] * len(height)
        cur_max = 0
        for i in range(len(height)):
            max_left[i] = cur_max
            cur_max = max(cur_max, height[i])
        
        # find max_right
        max_right = [0] * len(height)
        cur_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = cur_max
            cur_max = max(cur_max, height[i])

        for i in range(len(height)):
            # find amount of water at an index
            water = max(min(max_left[i], max_right[i]) - height[i], 0)
            maximum += water
        print("max_left", max_left)
        print("max_right", max_right)

        return maximum
"""
Goal: find max amount of rainwater that can be trapped between bars
- find the maximum on the left and the maximum on the right
- amount of water that can be trapped at a bar = min(leftmax, rightmax) - height
- if amount of water is negative, then 0
- update maximum
0   1   2   3   4   5   6   7   8   9
0   2   0   3   1   0   1   3   2   1

0   0   2   2   3   3   3   3   3   3 --> left max
3   3   3   3   3   3   3   2   1   0 --> right max

"""