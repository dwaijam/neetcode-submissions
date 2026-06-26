class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        left=0
        right=cols-1
        top = 1
        bottom = rows-1
        a, b = 0, 0
        dir = 1
        ans = []
        for _ in range(rows*cols):
            ans.append(matrix[a][b])
            if dir == 1:
                if b == right:
                    dir = 2
                    a+=1
                    right-=1
                else:
                    b+=1
            elif dir == 2:
                if a == bottom:
                    dir = 3
                    b-=1
                    bottom-=1
                else:
                    a+=1
            elif dir==3:
                if b==left:
                    dir=4
                    a-=1
                    left+=1
                else:
                    b-=1
            else:
                if a==top:
                    dir=1
                    b+=1
                    top+=1
                else:
                    a-=1
            print(a,b, dir)
        return ans  
                
