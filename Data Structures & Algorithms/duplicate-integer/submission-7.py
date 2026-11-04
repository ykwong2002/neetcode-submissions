class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Goal: check for duplicates in nums array
        - use a list
            key: number, val: count
        - if count > 0, return false

        initialise empty list
        iterate through list
        if num in list, return false
        """
        exist = []
        for num in nums:
            if num in exist:
                return True
            exist.append(num)
        return False