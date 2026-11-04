class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return
"""
Goal: find the 1-based indexes of numbers in numbers (sorted) to sum to target
- brute force: for each number, check the array to see if its counterpart is there --> O(n^2) solution
- since array is sorted, use 2 pointers:
    - if sum too big, move right pointer to left
    - if sum too small, move left pointer to right

1   2   3   4
l
        r
curr_sum = 5, too big --> move right pointer to left
curr_sum = 4 ...
"""