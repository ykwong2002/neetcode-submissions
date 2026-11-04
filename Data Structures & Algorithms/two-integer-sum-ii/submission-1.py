class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            curSum = numbers[i] + numbers[j]
            if curSum < target:
                i += 1
            elif curSum > target:
                j -= 1
                
        return [i + 1, j + 1]