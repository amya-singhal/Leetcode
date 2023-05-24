class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[1]*n] * m
        for m1 in range(1, m):
            for n1 in range(1, n):
                ans[m1][n1] = ans[m1 - 1][n1] + ans[m1][n1 - 1]
        return ans[-1][-1]
            
                
                
            