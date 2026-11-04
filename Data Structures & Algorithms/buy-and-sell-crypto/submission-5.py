class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = max_profit = 0

        for price in prices:
            # Update smallest
            smallest = min(smallest, price)

            if smallest < price:
                profit = price - smallest
                max_profit = max(max_profit, profit)
        
        return max_profit
"""
- update smallest
- if smallest < current, calculate profit and update max_profit
Goal: Find highest profit (greatest increase)
5   1   5   6   7   1
^

smallest = 0
profit = 0
max_profit = 0
"""
