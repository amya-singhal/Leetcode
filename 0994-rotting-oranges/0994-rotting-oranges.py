class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def check() -> bool:
            tmp = [a for b in grid for a in b]
            if 1 in tmp:
                return True
            return False
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        ans = 0
        while(q and check()):
            ans += 1
            for i in range(len(q)):
                (x, y) = q.pop(0)
                for i, j in directions:
                    newx = x + i
                    newy = y + j
                    if 0 <= newx < n and 0 <= newy < m and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        q.append((newx, newy))
        # print(grid)
        if check():
            return -1
        return ans
    
     