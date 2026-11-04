class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            # consider case of adding current number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # consider case of excluding current number
            cur.pop()
            # check if next number is same as current number
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
"""
Goal: return all combinations, each combination at most once
- backtracking since combinations
    - include current index
    - exclude current index

- initialise res array
- sort numbers so same numbers side by side
- dfs:
    - same as before, but now check if next number is same as curr number
- dfs(0, [], 0)
"""