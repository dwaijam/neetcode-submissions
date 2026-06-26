class Solution:
    def rob(self, nums: List[int]) -> int:

        
        
        def robHelper(st, en)->int:
            l = en-st+1
            if l==0:
                return 0
            elif l==1:
                return nums[st]
            elif l==2:
                return max(nums[st], nums[en])
            dp = [0] * len(nums)
            dp[st] = nums[st]
            dp[st+1] = max(nums[st+1], nums[st])
            for i in range(st+2,en+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[en]
        l = len(nums)
        if l == 0:
            return 0
        elif l==1:
            return nums[0]
        elif l==2:
            return max(nums[0], nums[1])
        
        return max(robHelper(0, l-2), robHelper(1, l-1))
            
