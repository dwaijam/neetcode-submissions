class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices)<=1:
            return 0
        mini = prices[0]
        for c in prices[1:]:
            profit = max(profit, c - mini)
            mini = min(mini, c)

        return profit
        