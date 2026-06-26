class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        
        def dfs(i, buying)-> int:
            if i>=len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            cool = dfs(i+1, buying)
            if buying:
                buysell = dfs(i+1, False) - prices[i]        
            else:
                buysell = dfs(i+2, True) + prices[i]

            return max(buysell, cool)

        return dfs(0, True)


