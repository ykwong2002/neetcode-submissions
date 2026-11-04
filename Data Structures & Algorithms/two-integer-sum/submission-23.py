class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            d[nums[i]] = i
"""
goal: have a target, return the indices of the array that sum to the target
brute force:
- for every number in array, go through every other number in the array, sum them, check if sum == target
3   4   5   6
^
    ^

optimal solution:
- if there is a target that a number needs to sum to, the complement of the target should be fixed for every number in the array
- d dictionary, number : index
- for every number:
    - find complement
    - check if complement is in d
    - if the complement is in d, then return (complement index, current index)
    - else, add to d
"""