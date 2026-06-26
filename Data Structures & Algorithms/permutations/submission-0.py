class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(cur: List[int], rem: List[int]):
            if len(rem) == 0:
                res.append(cur.copy())
            for i in range(len(rem)):
                cur.append(rem[i])
                helper(cur, rem[:i] + rem[i+1:])
                cur.pop()
        helper([], nums)
        return res

        