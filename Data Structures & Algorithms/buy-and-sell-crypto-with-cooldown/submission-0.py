class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        # returns profit
        def dfs(i, buying):
            # base case
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # if buying, got 2 choices --> buy or cooldown, then cache the higher profit
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)
            
        
"""
- if buy -> move i by 1
- if sell -> move i by 2
"""