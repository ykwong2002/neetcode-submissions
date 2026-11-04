class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        def dfs(i): # i represents the index of the element we are currently thinking of
            # base case: we exceed the length of the list
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # case of exploring branch with index
            subset.append(nums[i])
            dfs(i + 1)

            # case of exploring branch WITHOUT index
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
    
        return result
"""
Goal: return all possible subsets of nums
- binary tree: each level is another index
- perform recursive dfs twice:
    - once including the index
    - once NOT including the index
"""