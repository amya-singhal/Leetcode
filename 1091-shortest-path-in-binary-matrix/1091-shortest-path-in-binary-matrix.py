class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        grid[0][0] = 1
        directions = [(0,1), (0,-1), (1,0), (-1, 0), (1,1), (1,-1), (-1, 1), (-1, -1)]
        queue = collections.deque([(0,0,1)])
        while (queue):
            x, y, distance = queue.popleft()
            if (x, y) == (n-1, n-1):
                return distance
            for i, j in directions:
                xnew = x + i
                ynew = y + j
                if ((0 <= xnew < n) and (0 <= ynew < n) and (not grid[xnew][ynew])):
                    grid[xnew][ynew] = 1
                    queue.append((xnew, ynew, distance+1))
        return -1