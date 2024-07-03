class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l,r = 0, (row*col)-1
        while (l <= r):
            m = (l+r)//2
            curr = matrix[m // col][m % col]
            if target == curr:
                return True
            if target < curr:
                r = m-1
            else:
                l = m+1
        return False