class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        n = len(s)
        memo = [[None] * (n + 1) for _ in range(n + 1)]

        def dfs(i, open):

            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if memo[i][open] is not None:
                return memo[i][open]
            
            if s[i] == '(':
                res= dfs(i + 1, open + 1)
            elif s[i] == ')':
                res= dfs(i + 1, open - 1)
            else:
                res = (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))
            memo[i][open] = res
            return res

        def helper(open: int,  i: int) -> bool:
            if open < 0:
                return False
            if i >= len(s):
                return open == 0

            if s[i] == '(':
                return helper(open+1, i+1)
            elif s[i] == ')':
                return helper(open-1, i+1)
            else:
                return (helper(open, i+1) or helper(open+1, i+1) or helper(open-1, i+1))

        
        return dfs(0, 0)