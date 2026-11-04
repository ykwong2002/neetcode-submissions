class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1

"""
Goal: find target in logn time
- use binary search since array is sorted in asc
- find midpoint
    - if target < midpoint, repeat on first half
    - if target > midpoint, repeat on second half
-1  0   2   4   6   8
            ^
length of list = 6
midpoint index = 3
target = 0
since target < midpoint index, search on first half
"""