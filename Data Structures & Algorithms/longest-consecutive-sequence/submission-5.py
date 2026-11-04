class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0

        for num in nums:
            length = 1
            if (num - 1) not in unique: # start of a sequence
                while (num + length) in unique:
                    length += 1
                longest = max(longest, length)
        
        return longest
"""
Goal: return longest consecutive length (may not be in order in the original array)
- create a set for fast lookup
- MUST FIND START OF SEQUENCE!!!
- initialise longest variable to be returned
- for each number, check if n - 1 not in the set (indicates the start of a sequence):
    - length is 1
    - while number + length is in the set, length += 1
    - update longest if needed
- return longest

2   20   10  3   4   5
^
length = 4

longest = 4
"""