class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [... rob1, rob2, n, n + 1]
        for n in nums:
            # max we can rob until now
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
"""
Goal: find maximum we can rob from the array
- subproblem --> find maximum remaining
recurrence relationship:
    - rob = max(arr[0] + rob[2 : n], rob[1 : n])


- at position i, we update a new array with the maximum it can reach
1   2   3   1
1   2   4   4
"""