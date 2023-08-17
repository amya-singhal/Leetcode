class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            if cost[i] > gas[i]:
                continue
            t = 0
            s = 0
            for i in range(len(gas)):
                t += gas[i] - cost[i]
                if t < 0:
                    t = 0
                    s = i+1
            return s
                