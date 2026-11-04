class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set from array
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if n is start of sequence (does not have left neighbour)
            if (n - 1) not in numSet:
                length = 0
                # check if it has a right neighbour
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

