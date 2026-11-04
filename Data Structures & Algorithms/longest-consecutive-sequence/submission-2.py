class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # to create O(1) lookup
        longest = 0

        for num in nums:
            length = 1
            if (num - 1) not in nums: # if start of sequence
                while (num + length) in nums:
                    length += 1
            longest = max(longest, length)
        
        return longest
"""
Goal: find longest consecutive sequence of elements
- sorting is O(nlogn), not good enough
- a sequence only starts if num - 1 does not exist in array
- iterate through nums
    - length = 1
    - if num - 1 not in array (start of sequence)
        - while num + length in array:
            - length += 1

2   20  4   10  3   4   5
                ^
count = 0
max_count = 1
"""