class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        l = 0
        r = n-1
        while(l < r):
            for i in range(n):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1
        # print(matrix)
        """
        Do not return anything, modify matrix in-place instead.
        """
        