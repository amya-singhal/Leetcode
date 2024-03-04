class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        temperatures = [73,74,75,71,69,72,76,73]
        ans = [1,1,4,2,1,0,0]
        s = [6]
        i = 6
        """
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        s = [0]
        for i in range(1, n):
            while (s and temperatures[s[-1]] < temperatures[i]):
                x = s.pop()
                ans[x] = i-x
            s.append(i)
        return ans
            
        