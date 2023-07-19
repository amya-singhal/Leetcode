class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(matrix), len(matrix[0])
        longestPath = [[0] * n for _ in range(m)]
        
        def longestIncreasingPath_start(i, j) -> int:
            nonlocal matrix, directions, m, n, longestPath
            res = 1
            for direction in directions:
                pos = list(map(add, [i, j], direction))
                new_i, new_j = pos[0], pos[1]
                
                if new_i >= 0 and new_i < m and new_j >=0 and new_j < n and matrix[new_i][new_j] > matrix [i][j]:
                    if longestPath[new_i][new_j] == 0:
                        longestPath[new_i][new_j] = longestIncreasingPath_start(new_i, new_j)
                        
                    res = max(res, 1 + longestPath[new_i][new_j])
                longestPath[i][j] = res
            return res
        
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, longestIncreasingPath_start(i, j))
        return ans