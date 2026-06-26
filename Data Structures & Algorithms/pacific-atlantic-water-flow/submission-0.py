class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])
        pac = [[False] * self.cols for r in range(self.rows)]
        atl = [[False] * self.cols for r in range(self.rows)]
        ans = []

        def dfs(r, c, dp):
            if not dp[r][c]:
                dp[r][c]= True
                for a, b in (1,0), (-1, 0), (0, 1), (0, -1):
                    nr = r+a
                    nc = c+b
                    if nr < 0 or nc<0 or nr>=self.rows or nc>=self.cols:
                        continue
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, dp)


        for i in range(self.rows):
            dfs(i,0,pac)
            dfs(i, self.cols-1, atl)

        for j in range(self.cols):
            dfs(0, j, pac)
            dfs(self.rows-1, j, atl)

        for i in range(self.rows):
            for j in range(self.cols):
                if pac[i][j] and atl[i][j]:
                    ans.append([i,j])

        return ans

        