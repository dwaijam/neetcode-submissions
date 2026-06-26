class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            bt(i+1,cur)
            cur.pop()
            bt(i+1,cur)

        bt(0, [])
        return res