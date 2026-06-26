class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pre = [0] * (amount+1)
        cur = [0] * (amount+1)
        for i in range(len(coins)):
            cur[0] = 1
            for j in range(coins[i], amount+1):
                cur[j] = cur[j-coins[i]] + pre[j]
            print(cur)
            pre = cur

        return pre[amount]
            