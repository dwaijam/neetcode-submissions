class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(index: int, arr: list, sum: int):
            if sum == 0:
                res.append(arr.copy())
                return
            if index >= len(nums):
                return
            if nums[index]<=sum:
                arr.append(nums[index])
                helper(index, arr, sum-nums[index])
                arr.pop()
            
            helper(index+1, arr, sum)

        helper(0, [], target)
        return res
            