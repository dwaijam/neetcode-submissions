class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        if fresh == 0:
            return 0
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
                    if grid[r][c] == 1:
                        fresh-=1
                        grid[r][c] = 2
                        queue.append((r,c))

        if fresh!=0 :
            return -1
        else:
            return val-1
        

