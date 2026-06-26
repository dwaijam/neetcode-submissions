class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
            return False
        l = 0
        r = rows-1
        while l <= r:
            mid = (l+r)//2
            if target > matrix[mid][-1]:
                l=mid+1
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                break

        if l > r:
            return False
        col = (l+r)//2

        l,r = 0, cols
        while l <= r:
            mid = (l+r)//2
            if target > matrix[col][mid]:
                l = mid + 1
            elif target < matrix[col][mid]:
                r = mid-1
            else:
                return True

        return False

        
        