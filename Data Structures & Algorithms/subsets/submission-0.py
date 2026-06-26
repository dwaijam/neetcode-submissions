class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(index, cur:  List[int]):
            if index == len(nums):
                res.append(cur.copy())
                return
            helper(index+1, cur)
            cur.append(nums[index])
            helper(index+1, cur)
            cur.pop()
        
        helper(0, [])
        return res
            
        