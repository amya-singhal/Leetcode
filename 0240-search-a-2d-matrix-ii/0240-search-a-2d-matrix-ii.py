class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findTarget(row):
            # binary search
            l, r = 0, m-1
            while l < r:
                mid = (r+l) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    r = mid
                else:
                    l = mid+1
            return False
        
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[i][0] == target or matrix[i][m-1] == target:
                return True
            if matrix[i][0] <= target and matrix[i][m-1] >= target:
                if findTarget(i):
                    return True
        
        return False
                