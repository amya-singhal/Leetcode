class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjLst = [[] for i in range(n)]
        for x, y, d in flights:
            adjLst[x].append([y,d])
        # print(adjLst)
        distance = [float('inf') for i in range(n)]
        distance[src] = 0
        t = 0
        for i in range(k+1):
            tmp = distance.copy()
            for v in range(n):
                for y, length in adjLst[v]:
                    tmp[y] = min(tmp[y], distance[v]+length)
            distance = tmp    
        if distance[dst] == float('inf'):
            return -1
        return distance[dst]