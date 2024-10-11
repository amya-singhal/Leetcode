class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        direction = 0
        visited = set()
        x, y = 0,0
        start = 1
        for _ in range(n*n):
            # print(x, y, start, direction)
            matrix[x][y] = start
            visited.add((x, y))
            start += 1
            newx, newy = x + moves[direction][0], y + moves[direction][1]
            # print(newx, newy)
            if newx == -1 or newx == n or newy == -1 or newy == n or (newx, newy) in visited:
                direction = (direction+1)%4
            # print(direction)
            x, y = x + moves[direction][0], y + moves[direction][1]
            # print(x, y)
        return matrix