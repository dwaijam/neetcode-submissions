class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        rows = len(s1)
        cols = len(s2)
        if rows + cols != len(s3):
            return False
        dp = [[False] * (cols+1) for r in range(rows+1)]
        dp[0][0] = True
        for i in range(rows+1):
            for j in range(cols+1):
                t = i+j
                if i == 0:
                    if j> 0 and s3[j-1] == s2[j-1]:
                        dp[i][j] = dp[i][j-1]
                elif j == 0:
                    if i>0 and s3[i-1] == s1[i-1]:
                        dp[i][j] = dp[i-1][j]
                else:
                    if s3[t-1] == s2[j-1]:
                        dp[i][j] = dp[i][j] or dp[i][j-1]
                    if s3[t-1] == s1[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]


        print(dp)
        return dp[rows][cols]