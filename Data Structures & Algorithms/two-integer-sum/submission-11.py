class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Goal: find the 2 indexes in nums, whose values add up to target
        Naive:
        - at each index, check all other indexes
        - if current + pointer == target, return true
        - But this is O(n^2) cause of inner for loop (NOT GOOD)

        - Initialise a empty hashmap (compliment, store compliment of each num)
            - Key: Compliment, Val: Index
        - for each num in nums:
            - if num in compliment.vals
                - return [key, current index of num]
            - else:
                - add the index compliment pair to hashmap
        """
        d = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in d.keys():
                return [d[compliment], i]
            else:
                d[nums[i]] = i