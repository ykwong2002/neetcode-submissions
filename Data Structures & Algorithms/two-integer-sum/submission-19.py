class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return[d[complement], i]
            d[num] = i
"""
Goal: return indices of values that sum to target
brute force:
- for every number, iterate all other numbers to check if == target
- O(n^2)

- for every number, number needed is target - num
- track all numbers and their index in a dictionary
- if number exists, then return
0   1   2   3
3   4   5   6
d: (3, 0), 
"""