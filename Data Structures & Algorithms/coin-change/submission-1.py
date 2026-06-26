class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')] * (amount+1)
        arr[0] = 0
        for coin in coins:
            for j in range(amount+1):
                if j>=coin:
                    arr[j] = min(arr[j], arr[j-coin]+1)
        
        return arr[amount] if arr[amount]<float('inf') else -1