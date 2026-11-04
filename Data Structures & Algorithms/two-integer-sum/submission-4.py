class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create mapping
        d = {}
        
        # create mapping of num : index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in d:
                d[nums[i]] = i
            else:
                return [d[complement], i]
        
        return []