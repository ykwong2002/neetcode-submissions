class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1

        minimum = r
        l, r = 0, len(nums) - 1

        # Search right of pivot
        if target >= nums[minimum] and target <= nums[r]:
            l = minimum
        # Search left of pivot
        else:
            r = minimum - 1
        
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        return -1
"""
Goal: return index of target in nums, or -1
- use binary search to find pivot
- perform binary search on that half to find index

0   1   2   3   4   5
3   4   5   6   1   2
l
                    r
        m

"""