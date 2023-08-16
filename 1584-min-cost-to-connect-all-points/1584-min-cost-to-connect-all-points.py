class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # calculating ditance between two points
        def distance(a, b):
            return (abs(a[0]-b[0]) + abs(a[1]-b[1]))
        n = len(points)
        # calculating all edges
        d = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                dis = distance(points[i], points[j])
                d[i].append([dis, j])
                d[j].append([dis, i])
        # print(d)
        visited = set()
        result = 0
        h = [[0,0]]
        while(len(visited) < n):
            cost, point = heapq.heappop(h)
            if point in visited:
                continue
            visited.add(point)
            # print(cost, point)
            result += cost
            for l, neigh in d[point]:
                if neigh not in visited:
                    heapq.heappush(h, [l, neigh])
            # print(h)
        return result
                