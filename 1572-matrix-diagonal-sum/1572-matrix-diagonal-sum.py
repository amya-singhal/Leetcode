class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        d1 = 0
        d2 = len(mat[0]) - 1
        x = 0
        while (d1 != d2 and d2 != -1):
            ans += mat[x][d1]
            ans += mat[x][d2]
            d1 += 1
            d2 -= 1
            x += 1
        if (d2 == -1):
            return ans
        ans += mat[x][d1]
        d1 += 1
        d2 -= 1
        x += 1
        while (d2 != -1):
            ans += mat[x][d1]
            ans += mat[x][d2]
            d1 += 1
            d2 -= 1
            x += 1
        return ans
            
            
                    
                
        