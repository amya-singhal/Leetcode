class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        count = [0]*60
        
        for i in range(len(time)):
            needed = time[i] % 60
            ans += count[(60- needed)% 60]
            count[needed] += 1
        return ans