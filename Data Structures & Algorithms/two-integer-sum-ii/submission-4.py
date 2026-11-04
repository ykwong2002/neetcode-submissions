class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while True:
            temp = numbers[l] + numbers[r]
            if temp > target:
                r -= 1
            elif temp < target:
                l += 1
            else:
                break
        
        return [l + 1, r + 1]
"""
Goal: find the pair in numbers that add up to target
- since non-decreasing, can use 2 pointers

1   2   3   4
l       r
sum = 4
"""