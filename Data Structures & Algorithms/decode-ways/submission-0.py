class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i>=len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            onechar = dfs(i+1)
            if s[i] == '1' and i+1<len(s):
                onechar+= dfs(i+2)
            if s[i] == '2' and i+1<len(s) and int(s[i+1]) >=0 and  int(s[i+1])<=6:
                onechar+= dfs(i+2)
            memo[i] = onechar
            return onechar

        return dfs(0)