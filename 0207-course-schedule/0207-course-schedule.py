class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        indegrees = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            indegrees[course] += 1
        q = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        visited = set()       
        while q:
            for _ in range(len(q)):
                course = q.pop(0)
                visited.add(course)
                for x in graph[course]:
                    if x not in visited:
                        indegrees[x] -= 1
                        if indegrees[x] == 0:
                            q.append(x)
        if len(visited) == numCourses:
                return True
        return False
        