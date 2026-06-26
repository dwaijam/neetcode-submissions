class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        sq = [[False] * 9 for _ in range(9)]

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])-1
                if rows[i][num]:
                    return False
                rows[i][num] = True
                if cols[j][num]:
                    return False
                cols[j][num] = True
                sqn = 3*(i//3) + j//3
                if sq[sqn][num]:
                    return False
                sq[sqn][num] = True
            
        return True