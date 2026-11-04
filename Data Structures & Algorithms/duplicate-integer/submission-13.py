class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            if num in unique:
                return True # appears more than onec
            unique.add(num)
        
        return False
"""
Goal: return boolean on whether or not a number appears more than once
- initialise a set to store unique numbers
- if number is in set (fast look up): return True since duplicate exists
- else: add number to set
- return False
"""