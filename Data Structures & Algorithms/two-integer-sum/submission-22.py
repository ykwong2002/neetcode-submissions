class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i
"""
Goal: return indices i and j such that nums[i] + nums[j] = target
- create a hashmap for nums : index
- for each number:
    - find the complement (number that needs to sum to target)
    - if complement exists, return both numbers
    - if complement does not exist, add the (number : index) pair to the hashmap
"""