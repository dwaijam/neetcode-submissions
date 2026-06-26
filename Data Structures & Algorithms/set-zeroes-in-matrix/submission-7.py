class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        j0 = False
        i0=False
        for i in range(rows):
            if matrix[i][0] == 0:
                i0=True
                break
        for j in range(cols):
            if matrix[0][j] == 0:
                j0=True
                break
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0] == 0 or matrix[0][j] ==0:
                    matrix[i][j] = 0

        print(matrix, i0, j0)
        if i0:
            for i in range(rows):
                matrix[i][0] = 0
        print(matrix)
    
        if j0:
            for j in range(cols):
                matrix[0][j] = 0
        print(matrix)
                
                    