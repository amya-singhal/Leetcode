class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        longestPath = [[0 for _ in range(m+1)] for _ in range(n+1)]
        ans = 0
        def helper(i, j):
            val = matrix[i][j]
            maxi = 0
            for x,y in directions:
                newi, newj = i+x, j+y
                if 0 <= newi < n and 0 <= newj < m and matrix[newi][newj] > val:
                    if longestPath[newi][newj] == 0:
                        longestPath[newi][newj] = helper(newi, newj)
                    maxi = max(longestPath[newi][newj], maxi)
            return maxi+1
        for i in range(n):
            for j in range(m):
                ans = max(ans, helper(i, j))
        return ans