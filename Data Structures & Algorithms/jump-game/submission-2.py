class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        i = 0
        while i <=mx and i<len(nums):
            mx = max(mx, nums[i] + i)
            if mx >= len(nums)-1:
                return True
            i+=1

        return False

        