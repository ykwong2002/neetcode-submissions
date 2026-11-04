class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            # identify complement of the number to sum to target
            complement = target - nums[i]

            # if complement is already in d, return ans
            if complement in d:
                return [d[complement], i]
            
            # if complement not in d, add the complement as well as its index
            else:
                d[nums[i]] = i