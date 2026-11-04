class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                update_index, update_temp = stack.pop()
                output[update_index] = i - update_index
            stack.append((i, temp))
        
        return output