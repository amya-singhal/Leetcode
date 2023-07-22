class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        # to make adj List
        for x, y in prerequisites:
            graph[y].append(x)
        # to detect if there is a cycle in the graph
        visited = [0]*numCourses
        ans = []
        def dfs(index, visited):
            if visited[index] == -1:
                return False
            if visited[index] == 1:
                return True
            visited[index] = -1
            for neigh in graph[index]:
                if not dfs(neigh, visited):
                    return False
            ans.append(index)
            visited[index] = 1
            return True
        for n in range(numCourses):
            if not dfs(n, visited):
                return []
        return ans[::-1]