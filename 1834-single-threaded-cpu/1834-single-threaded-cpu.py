class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        h = [[1,2],[2,4],[3,2],[4,1]]
        h2 = [[7,2],[7,4],[7,5],[7,10],[7,12]]
        track = 3
        """
        sortedTasks = sorted((task[0], task[1], i) for i, task in enumerate(tasks))
        # print(sortedTasks)
        startTime = 0
        index = 0
        heap = []
        ans = []
        while len(ans) < len(tasks):
            while index < len(tasks) and sortedTasks[index][0] <= startTime:
                heapq.heappush(heap, (sortedTasks[index][1], sortedTasks[index][2], sortedTasks[index][0]))
                index += 1
                
            if heap:
                processtime, i,enquetime = heapq.heappop(heap)
                ans.append(i)
                startTime += processtime
            else:
                startTime = sortedTasks[index][0]
        
        while index < len(tasks):
            ans.append(index)
            index += 1
        return ans   
        