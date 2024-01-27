class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        [[1,3,1],[1,5,1],[4,2,1]]
        cache = {(1,1): 6}
        q = [(2,0) (1,1) (0,2)]
        
        down -> (0,1), right -> (1,0)
        """
        cache = defaultdict(int)
        m = len(grid)
        n = len(grid[0])
        q = [[0,0]]
        cache[(0,0)] = grid[0][0]
        directions = [(1,0), (0,1)]
        while len(q) > 0:
            x,y = q.pop(0)
            pathValue = cache[(x,y)]
            for i,j in directions:
                newx, newy = x+i, y+j
                if 0 <= newx < m and 0 <= newy < n:
                    if (newx, newy) in cache:
                        cache[(newx, newy)] = min(pathValue+grid[newx][newy], cache[(newx, newy)])
                    else:
                        cache[(newx, newy)] = pathValue+grid[newx][newy]
                        q.append([newx, newy])
        return cache[(m-1, n-1)]
                            
                        
                        
                    
        