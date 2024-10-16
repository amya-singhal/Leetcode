class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def BFS(building_r, building_c):
            """
            for a given building coordinate, find the min. distance to reach this very building,
            while considering all the previous buildings discovered so far.
            """
            min_distance = math.inf
            # the 3rd element "0" is how many steps to reach the building.
            # since we start at the building itself, it's 0 steps to begin with.
            queue = [[building_r, building_c, 0],] 
            while queue:
                r, c, steps_so_far = queue.pop(0)
                for i in range(4):
                    rr = r + r_direction[i]
                    cc = c + c_direction[i]
                    # skip out-of-bound coordinates
                    if 0 > rr or rr >= m or 0 > cc or cc >= n:
                        continue
                    if grid[rr][cc] == emptyLandValue:
                        total_distance_sum[rr][cc] += (steps_so_far+1)
                        min_distance = min(min_distance, total_distance_sum[rr][cc])
                        queue.append([rr, cc, steps_so_far+1])
                        grid[rr][cc] = emptyLandValue - 1 # the trick
            return min_distance
        
        # set up
        m, n = len(grid), len(grid[0])
        total_distance_sum = [[0] * n for _ in range(m)]
        r_direction = [+1, -1, 0, 0]
        c_direction = [0, 0, +1, -1]
        
		# update the total_distance_sum matrix and the min_distance iteratively for all buildings
        emptyLandValue, buildingValue = 0, 1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == buildingValue:
                    min_distance = BFS(row, col) # tracking the min distance so far
                    if min_distance == math.inf:
                        return -1
                    emptyLandValue -= 1 # the trick
        return min_distance