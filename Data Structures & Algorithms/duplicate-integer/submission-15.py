class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        
        return False
"""
Goal: return true if there is a duplicate
- use a set to track (for fast lookup --> O(n))
"""