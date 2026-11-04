class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # find the minimum first
        while l < r:
            m = l + ((r - l)) // 2 # midpoint
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        pivot = l # minimum of array is at index l
        l, r = 0, len(nums) - 1 # binary search from pivot

        if target >= nums[pivot] and target <= nums[r]: # belongs on right of pivot
            l = pivot
        else: # belongs on left of pivot
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1
