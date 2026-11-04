class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = a + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return result
"""
Goal: return a list of lists (triplets that sum to 0)
- sort the list
- for each number:
    - if number same as previous number, skip
    - consider a 2 pointer for the remaining numbers

-4  -1  -1  0   1   2
^       l           r
curr_sum = -4-1+2 = -3
if curr_sum < 0, move left pointer
if curr_sum > 0, move right pointer
if curr_sum == 0, append to result list, move left and right pointer as there may be more combinations
"""