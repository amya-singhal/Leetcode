class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonalSum = 0
        for i in range(0, n):
            diagonalSum += mat[i][i]
            if i != n-i-1:
                diagonalSum += mat[i][n-i-1]
        return diagonalSum