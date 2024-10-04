class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        h = [(-1, 0)]
        visited = {}
        while heap:
            pop from heap
            if end_node == pop:
                update global -prob
            unvisited neighbors, add them to the heap
        """
        graph = defaultdict(set)
        for i in range(len(edges)):
            x, y = edges[i]
            prob = succProb[i]
            graph[x].add((y, prob))
            graph[y].add((x, prob))
        # {0: [(1, 0.5), (2, 0.3)], ....}  
        # print(graph)
        heap = [[-1, start_node]]
        visited = set()
        while heap and len(visited) != n:
            # print(heap)
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -1*curr_prob
            visited.add(node)
            if node == end_node:
                return curr_prob
                max_prob = max(max_prob, curr_prob)
            for neigh in graph[node]:
                neighNode, neighProb = neigh
                neighProb = neighProb
                if neighNode not in visited:
                    heapq.heappush(heap, [(-1*curr_prob*neighProb), neighNode])
        return float(0)
        