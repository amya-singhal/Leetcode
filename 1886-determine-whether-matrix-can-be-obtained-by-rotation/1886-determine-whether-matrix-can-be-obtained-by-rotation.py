class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True
        rotate = 3
        while(rotate > 0):
            for i in range(n):
                for j in range(i):
                    if i != j:
                        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            l = 0
            r = n-1
            while(l < r):
                for i in range(n):
                    mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
                l += 1
                r -= 1
            if target == mat:
                return True
            rotate -= 1
        return False
            