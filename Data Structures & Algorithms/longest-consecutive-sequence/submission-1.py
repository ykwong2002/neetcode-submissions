class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet: # check if n is start of sequence (does not have left neighbour)
                length = 0
                while (n + length) in numSet: # check if it has a right neighbour
                    length += 1
                longest = max(longest, length)
        
        return longest

