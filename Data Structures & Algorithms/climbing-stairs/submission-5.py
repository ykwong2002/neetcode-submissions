class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if n == 1 or n == 2:
            return n
        
        dp = [0] * (n + 1)

        # initialise the base case values
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[ i - 2]
        
        return dp[n]
"""
Goal: find number of distinct ways to reach top of stairs
- from a step i:
    - can take 2 steps from i - 2
    - can take 1 step from i - 1
- base case: n == 1 --> 1 way to climb
- base case: n == 2 --> 2 ways to climb (2 1 steps or 1 2 step)
- use a dp array to track the values
"""