class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        visited = set()
        val=0
        while queue:
            l = len(queue)
            val+=1
            print(queue)
            for i in range(l):
                pop = queue.popleft()

                for a,b in (1,0), (-1,0), (0, 1), (0, -1):
                    r = pop[0] + a
                    c = pop[1] + b
                    if r< 0 or c<0 or r>=rows or c>=cols:
                        continue
                    if grid[r][c] == 2147483647:
                        grid[r][c] = val
                        queue.append((r,c))
        



