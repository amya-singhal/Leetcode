class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        ["A","A","A", "B","B","B"], n = 3 --> 10
        ["A","C","A","B","D","B"], n = 1 --> 6
        ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"] 2
        count = a:1, b:2
        ans = [a, b, idle, idle, a, b, ]
        tmp = 1
        s = [a,b]
        """
        task_counts = Counter(tasks)
        maxFreq = max(task_counts.values())
        maxCount = sum(1 for count in task_counts.values() if count == maxFreq)
        
        minIntervals = (maxFreq - 1) * (n + 1) + maxCount
        
        return max(len(tasks), minIntervals)