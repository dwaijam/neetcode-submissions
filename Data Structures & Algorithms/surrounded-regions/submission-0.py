class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(r, c):
            if r< 0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c] != "O":
                return
            board[r][c] = "Y"
            for a, b in (1,0), (-1, 0), (0, 1), (0, -1):
                dfs(r+a, c+b)

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
        
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"

        

            
        