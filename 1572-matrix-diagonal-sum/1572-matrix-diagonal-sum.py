class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonalSum = 0
        l = 0
        r = len(mat) - 1
        while (l < len(mat) and r >= 0):
            diagonalSum += mat[l][l]
            if l != r:
                diagonalSum += mat[l][r]
            l += 1
            r -= 1
        return diagonalSum