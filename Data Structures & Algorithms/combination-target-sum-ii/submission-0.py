class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def helper(i: int, target: int, arr: list):
            if target==0:
                ans.append(arr.copy())
                return
            elif i>= len(candidates) or candidates[i] > target:
                return
            
            arr.append(candidates[i])
            helper(i+1, target - candidates[i], arr)
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, target, arr)

        helper(0, target, [])
        return list(ans)
