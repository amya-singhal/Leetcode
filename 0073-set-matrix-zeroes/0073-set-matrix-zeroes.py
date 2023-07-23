class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for j in range(n):
            for r in row:
                matrix[r][j] = 0
        for i in range(m):
            for c in col:
                matrix[i][c] = 0
            
        """
         Do not return anything, modify matrix in-place instead.
        """
        