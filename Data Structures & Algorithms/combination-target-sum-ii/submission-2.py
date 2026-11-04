class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # consider case of including current index and move to next one            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            # consider case of skipping current index
            while (i + 1 < len(candidates)) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return result
"""
Goal: find unique combinations of candidates to sum to target, but each element chosen at most once
- think of it as binary tree, at each level, stop or continue adding more elements
- initialise global result variable
- keep track of current index i, cur subset list, total of cur

- sort the list to ensure duplicates are adjacent
- base case: if total == target: add cur to result and break (since adding more will exceed)
- base case: if total > target or i >= len(candidates): break immediately (since exceed already or no more to consider)
- recursive step:
    consider case of including the current index:
        cur.append(candidates[i])
        dfs(i + 1, cur, total += candidates[i])
    
    consider case of excluding current index:
        while same number as previous, keep shifting pointer (to avoid duplicates)
        cur.append(candidates[i])
        dfs(i, cur, total)
dfs(0, [], 0)
return result
"""