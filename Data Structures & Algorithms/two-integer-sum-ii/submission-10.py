class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
"""
Goal: return indices of the sorted array such that the elems add up to target
- since sorted --> use 2 pointers
- if curr_sum too big, reduce r pointer
- if curr_sum too small, increase l pointer

1   2   3   4
l
            r
"""