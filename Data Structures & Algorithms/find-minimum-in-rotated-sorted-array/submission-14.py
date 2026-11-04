class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
"""
0   1   2   3   4   5
3   4   5   6   1   2
                l
                r
            m
Goal: Find min of nums given that its been rotated
- use binary search to find the midpoint
- if midpoint < right: go left (wrap is on the left)
- if midpoint > right: go right (wrap is on the right)
"""