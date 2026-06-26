class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(op:int, cl: int, s: str)->List[str]:
            res = []
            if op == 0 and cl == 0:
                return [s]
            if op > 0:
                res.extend(dfs(op-1, cl, s+"("))
            if cl > op:
                res.extend(dfs(op, cl-1, s+")"))
            return res

        return dfs(n, n, "")
