class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create hashtable
        res = [1] * len(nums)

        # prefix pass (before index)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # previous index prefix
            prefix *= nums[i] # update prefix
        
        # postfix pass (after index)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # next index postfix
            postfix *= nums[i] #update postfix
        
        return res

