class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        minute = 0
        q = []
        def check() -> bool:
            tmp = [a for b in grid for a in b]
            if 1 in tmp:
                return False
            return True

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
        while (q and not check()):
            for _ in range(len(q)):
                (x,y) = q.pop(0)
                for a, b in directions:
                    newx = a+x
                    newy = b+y
                    if 0 <= newx < n and 0 <= newy < m and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        q.append((newx, newy))
            minute += 1
        if not check():
            return -1
        return minute
    