class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]

        for sell in prices:
            profit = max(profit, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return profit
