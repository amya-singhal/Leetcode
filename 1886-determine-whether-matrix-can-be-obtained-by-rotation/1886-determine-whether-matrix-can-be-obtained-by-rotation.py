class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        x =0
        if (len(mat) == 0):
            return True
        while(x < 4):
            l = 0
            r = len(mat)-1
            while(l <= r) :
                mat[l], mat[r] = mat[r], mat[l]
                l += 1
                r -= 1
            # transpose
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            if (mat == target):
                return True
            x += 1
        return False
                    