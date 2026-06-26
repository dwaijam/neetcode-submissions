class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        mx = float('-inf')
        cursum = 0
        for n in nums:
            cursum = max(cursum+n, n)
            mx = max(cursum, mx)

        return mx

        