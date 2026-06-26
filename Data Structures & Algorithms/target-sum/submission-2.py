class Solution:
    def findTargetSumWays(self, nums: List[int], t: int) -> int:
        total = sum(nums)

        if t > total:
            return 0
        target = (total + t) // 2
        if (total + t)%2!=0:
            return 0



        dp = [0]*(target+1)
        dp[0] = 1

        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j]+dp[j-num]

        return dp[target]

        