class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        mx_step = nums[0]
        prev = 1
        step = 0
        done = True
        while prev < len(nums):
            step+=1
            last = min(mx_step, len(nums)-1)
            for j in range(prev, last+1):
                mx_step = max(mx_step, j + nums[j])
            prev = last + 1
            
        return step