class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = {}
        self.mx = 0
        def dfs(r, c, num):
            if r < 0 or r>= len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!=1:
                return
            grid[r][c]= -1
            area[num] = area.get(num,0)+1
            self.mx = max(self.mx,area[num] )
            for a,b in (1,0), (-1,0), (0, 1), (0, -1):
                dfs(r+a, c+b, num)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count+=1
                    dfs(i, j, count)
        
        return self.mx