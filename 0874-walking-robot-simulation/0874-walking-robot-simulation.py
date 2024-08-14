class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacleSet = set(tuple(_) for _ in obstacles)
        # map, key is direction, value is tuple of left and right directions
        x, y, dx, dy = 0,0,0,1
        res = 0
        for command in commands:
            if command == -1:
                dx, dy = dy, -dx
            elif command == -2:
                dx, dy = -dy, dx
            else:
                for _ in range(command):
                    newx, newy = x+dx, y+dy
                    if (newx, newy) in obstacleSet:
                        break
                    x,y = newx, newy
                res = max(res, x*x+y*y)  
        return res