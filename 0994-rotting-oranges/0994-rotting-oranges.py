class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def check() -> bool:
            temp = [a for b in grid for a in b]
            if 1 in temp: 
                return True
            return False
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes = 0
        while(q and check()):
            minutes += 1
            for i in range(len(q)):
                x, y = q.pop(0)
                for i, j in directions:
                    xNew = x + i
                    yNew = y + j
                    if (0 <= xNew < len(grid) and 0 <= yNew < len(grid[0]) and grid[xNew][yNew] == 1):
                        grid[xNew][yNew] = 2
                        q.append((xNew, yNew))
        if check():
            return -1
        return minutes
                    