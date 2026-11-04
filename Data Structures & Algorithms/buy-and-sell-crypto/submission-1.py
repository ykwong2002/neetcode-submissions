class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]

        for sell in prices:
            profit = max(profit, sell - minBuy) # max profit is larger between diff and prev profit
            minBuy = min(minBuy, sell) # minBuy is the smaller between both buy and sell
        
        return profit
