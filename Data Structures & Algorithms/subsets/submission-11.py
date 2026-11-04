class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # explores branch including i
            subset.append(nums[i])
            dfs(i + 1)
            # explores branch excluding i
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
"""
Goal: return all possible combinations of nums
e.g [1, 2, 3]
[], [1], [2], [3], [1, 2], [1, 3]...
- for each number, there are 2 possible paths:
    - INCLUDING the number
    - EXCLUDING the number

- initialise a result array
- initialise a subset array
- for each number:
    - if reach end of the list:
        - add subset to result
    - recursively explore branch including
    - pop from subset
    - recursively explore branch excluding
"""