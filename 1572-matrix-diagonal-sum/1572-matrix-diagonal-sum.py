class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        d2 = len(mat[0]) - 1
        x = 0
        while (d2 != -1):
            if (x == d2):
                ans += mat[x][x]
            else:
                ans += mat[x][x]
                ans += mat[x][d2]
            d2 -= 1
            x += 1
        return ans
            
            
                    
                
        