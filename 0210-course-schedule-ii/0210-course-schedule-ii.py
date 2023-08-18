class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        for i,j in prerequisites:
            adjList[j].append(i)
        # print(adjList)
        indeg = [0]*numCourses
        for i in range(numCourses):
            for x in adjList[i]:
                indeg[x] += 1
        # print(indeg)
        h = []
        for i in range(len(indeg)):
            if indeg[i] == 0:
                h.append(i)
        ans = []
        # print(h)
        while(h):
            for i in range(len(h)):
                x = h.pop(0)
                ans.append(x)
                for neigh in adjList[x]:
                    indeg[neigh] -= 1
                    if indeg[neigh] == 0:
                        h.append(neigh)
            # print(indeg)
        for i in range(numCourses):
            if indeg[i] != 0:
                return []        
        return ans