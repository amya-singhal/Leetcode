class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0]*n
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        # sorted_indegree = sorted(indegree)
        heap = []
        for i in range(len(indegree)):
            heapq.heappush(heap, (-indegree[i], i))
        
        values = [0]*n
        value = n
        for i in range(len(indegree)):
            val, i = heapq.heappop(heap)
            values[i] = value
            value -= 1
        ans = 0
        for x,y in roads:
            ans += (values[x]+values[y])
            
        return ans
        

        
        