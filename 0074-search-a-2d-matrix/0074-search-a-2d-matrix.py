class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = len(matrix)
        b = len(matrix[0])
        if a == 1 and b == 1:
            if matrix[0][0] != target:
                return False
            else:
                return True
        # print(a, b)
        l = 0
        r = len(matrix)-1
        while(l<r):
            m = (l+r)//2
            if matrix[m][b-1] == target:
                return True
            if matrix[m][0] <= target and matrix[m][b-1] > target:
                l = m
                break
            elif matrix[m][b-1] > target:
                r = m - 1
            else:
                l = m + 1
        l1 = 0
        r1 = len(matrix[0])-1
        while(l1 < r1):
            m1 = (l1+r1)//2
            if matrix[l][m1] == target:
                return True
            elif matrix[l][m1] > target:
                r1 = m1 - 1
            else:
                l1 = m1 + 1
        if matrix[l][l1] == target:
            return True
        return False
            