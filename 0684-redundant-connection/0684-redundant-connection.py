class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegrees = defaultdict(int)
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegrees[x] += 1
            indegrees[y] += 1
        # print(graph)
        # {1:2,4,5, 2:1,3, 3:2,4, 4:1,3, 5:1}
        q = []
        for i in indegrees:
            if indegrees[i] == 1:
                q.append(i)
        while q:
            #print(q)
            x = q.pop(0)
            indegrees[x] -= 1
            for neigh in graph[x]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 1:
                    q.append(neigh)
        for x,y in edges[::-1]:
            if indegrees[x] == 2 and indegrees[y]:
                return [x,y]