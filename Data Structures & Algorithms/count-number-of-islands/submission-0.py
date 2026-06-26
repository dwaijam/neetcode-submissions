class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def dfs(r, c):
            if r < 0 or r>= len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!="1":
                return
            grid[r][c]="c"
            for a,b in (1,0), (-1,0), (0, 1), (0, -1):
                dfs(r+a, c+b)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count+=1
                    dfs(i, j)
        
        return count