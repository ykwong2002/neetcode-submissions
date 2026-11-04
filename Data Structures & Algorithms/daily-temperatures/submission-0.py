class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures): # day : temp
            while stack and t > stack[-1][0]:
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append((t, i))
        
        return res