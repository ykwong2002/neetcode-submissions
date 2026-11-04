class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            d[nums[i]] = i
"""
Goal: return pair of indices that sum to target
- initialise dictionary d
- complement = target - num
- check if complement is in d
    - if inside: return the indices
    - if not inside: add number and index to the dictionary
"""