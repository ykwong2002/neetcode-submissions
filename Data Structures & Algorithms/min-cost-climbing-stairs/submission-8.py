class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        base case:
        min(2, 3)

        dp[i] represents the minimum cumulative cost to reach step i
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        """
        n = len(cost)
        if n == 2:
            return min(cost)
        
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]