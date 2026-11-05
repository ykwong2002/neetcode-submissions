class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # prefix pass
        carry = 1
        for i in range(len(nums)):
            res[i] = carry
            carry *= nums[i]
        
        # postfix pass
        carry = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= carry
            carry *= nums[i]
        
        return res
"""
goal: given an array nums, return an array where the output of this new array is the product of all elements in nums except the element at index i itself

brute force:
- create an output array
- for each element:
    - go through all other elements
    - if element is current element, then skip, then multiply all the others together

smarter option:
- get product of all elements in nums
- go through each of the elements in 
- account for zero division

smartest option:
- 2 passes:
- at every single index i, value = prefixes * postfixes

- initialise a 1 --> used to carry over into next index
prefix pass:
for i in range(len(arr)):
    carry = carry * arr[i]
    res[i] = carry

carry = 1
postfix pass:
for i in range(len(arr) - 1, 0, -1)
- 
res 1   1   2   8
og  1   2   4   6
    ^
carry = 1
"""