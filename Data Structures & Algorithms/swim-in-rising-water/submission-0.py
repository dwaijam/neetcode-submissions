class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mx = 0
        minheap = [(grid[0][0], 0, 0)]
        while heapq:
            print(minheap)
            val, i, j = heapq.heappop(minheap)
            grid[i][j] = float('inf')
            mx = max(mx, val)
            if i == rows-1 and j==cols-1:
                break
            for a,b in (1,0), (-1,0), (0, 1), (0,-1):
                r = i+a
                c = j+b
                if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == float('inf'):
                    continue
                heapq.heappush(minheap, (grid[r][c], r, c))
        return mx

        