class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #bfs
        graph = [[] for i in range(numCourses)]
        # to make adj List
        for x, y in prerequisites:
            graph[y].append(x)
        # print(graph)
        # visited, and indeg array
        visited = [0]*numCourses
        indeg = [0]*numCourses
        for g in range(numCourses):
            for x in graph[g]:
                indeg[x] += 1
        # print(indeg)
        q = []
        for g in range(numCourses):
            if indeg[g] == 0:
                q.append(g)
        # print(q)
        ans = []        
        while q:
            element = q.pop(0)
            ans.append(element)
            # print(graph[element])
            for x in graph[element]:
                indeg[x] -= 1
                if indeg[x] == 0:
                    q.append(x)
        if len(ans) != numCourses:
            return []
        return ans 