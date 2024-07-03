class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        l,r = 0, n-1
        reqRow = -1
        while (l <= r):
            mid = (l+r) // 2
            if matrix[mid][0] <= target <= matrix[mid][m-1]:
                reqRow = mid
                break
            if l == mid and r == mid:
                return False
            elif target > matrix[mid][m-1]:
                l = mid + 1
                reqRow = l
            else:
                r = mid - 1
        l,r = 0, m-1
        while (l <= r):
            mid = (l+r) // 2
            if matrix[reqRow][mid] == target:
                return True
            elif target > matrix[reqRow][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
        