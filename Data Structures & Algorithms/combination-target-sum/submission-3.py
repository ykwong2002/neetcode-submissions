class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base case once target is reached
            if total == target:
                res.append(cur.copy())
                return
            
            # base case where cannot continue anymore
            if i >= len(nums) or total > target:
                return
            
            # consider case of including candidate (continue including occurences of i)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # consider case without candidate (move on to next index i)
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
"""
Goal: find all combinations of nums (can repeat) to add up to target
- initialise global result
- initialise an empty subset
- think of it as a binary tree --> at each level, choose to include OR exclude current index
- perform dfs on subset: if exceed, return. if match target, add to result, return
    - perform dfs with and without the current index
"""