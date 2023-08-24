class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        d = defaultdict(list)
        for i in range(n):
            for j in range(m):
                diagonalIndex = i-j
                d[diagonalIndex].append(mat[i][j]) 
        for key in d:
            d[key].sort(reverse=True)
        for i in range(n):    
            for j in range(m):
                diagonalIndex = i-j
                element = d[diagonalIndex].pop()
                mat[i][j] = element
        return mat
                
                
            