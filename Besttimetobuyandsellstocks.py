class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_till_now = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            min_till_now = min(min_till_now, prices[i])
            max_profit = max(max_profit, prices[i] - min_till_now)
        return max_profit
