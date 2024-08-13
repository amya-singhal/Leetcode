class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowersPlotted = 0
        flowerbeds = [0] + flowerbed + [0]
        for i in range(1, len(flowerbeds)-1):
            if flowerbeds[i-1] == 0 and flowerbeds[i] == 0 and flowerbeds[i+1] == 0:
                flowersPlotted += 1
                flowerbeds[i] = 1
        return flowersPlotted >= n
                
        