class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            # if complement does not exist, add it and its index to the map
            d[nums[i]] = i
"""
Goal: return the indices that sum up to target, smaller index first
- brute force: for every number, check all other numbers to see if it sums --> O(n^2) inefficient
- use hashmap
- for each number:
    - check hashmap if the complement exists
    - if exists, return the indices
    - if does not exist, add to hashmap the value : index pair
"""