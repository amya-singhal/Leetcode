class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 0,4,3,0
        t, r, b, l = 0, len(matrix[0]), len(matrix), 0
        # print(t, r, b, l)
        ans = []
        while t < b and l < r:
            for i in range(t, r):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                ans.append(matrix[i][r-1])
            r -= 1
            if not (l < r and t < b):
                break
            for i in range(r-1, l-1, -1):
                ans.append(matrix[b-1][i])
            b -= 1
            for i in range(b-1, t-1, -1):
                ans.append(matrix[i][l])
            l += 1
        return ans
