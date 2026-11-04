class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base case 1
            if total == target:
                res.append(cur.copy())
                return
            # base case 2
            if total > target or i == len(nums):
                return
            
            # include more occurences of i
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # exclude more occurences of i
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)

        return res
"""
Goal: return all combinations of nums that sum to target
- backtracking:
    - continue including occurences of current number
    - exclude any further occurences of current number

- initialise a res array
- perform dfs w 3 inputs:
    - current index i
    - current subset cur[]
    - total of current subset total
- in dfs function:
    - base case: total == target: add cur to res
    - base case: total > target: return (stop)
    - recursive relation 1: include more occurences of index i
    - recursive relation 2: exclude more occurences of index i


dfs(0, [], 0)
"""