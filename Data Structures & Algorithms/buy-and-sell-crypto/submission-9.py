class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for r in range(len(prices)):
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)
            while prices[r] < prices[l] and l < r:
                l += 1
            print("curr_profit", curr_profit)
        return max_profit
"""
Goal: return maximum profit buy buying on one day and selling on another (buy < sell)
- initialise max_profit as 0
- sliding window
- for r in range(len(prices) - 1):
    - calcaulate curr profit
    - update max profit
    - while prices[r] < prices[l] and l <= r: increment left pointer
5   1   5   6   7   1   10
    l
                    r
max_profit = 6
curr_profit = 0
"""