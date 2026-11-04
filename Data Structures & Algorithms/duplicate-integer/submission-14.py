class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for num in nums:
            if num in unique:
                return True
            unique.add(num)

        return False
"""
Goal: return True if value appears more than once, false eitherwise
- maintain a set of numbers that have appeared
- if appeared, return True (duplicate)
- if has not appeared, add to set
"""