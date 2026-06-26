class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums)
        for i in range(1, len(nums)): # 1, 1, 2, 8
            p[i] = p[i-1] * nums[i-1]

        ans = [1] * len(nums)
        ans[len(nums)-1] = p[len(nums)-1]
        back = 1
        for j in range(len(nums)-2, -1, -1): # 48
            back = back * nums[j+1]
            ans[j] = back * p[j]
        
        return ans
            