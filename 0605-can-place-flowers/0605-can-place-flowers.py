class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowersPlotted = 0
        i = 0
        allowed = True
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i] == 0:
                if i-1 >= 0 and flowerbed[i-1] == 1:
                    i += 1
                    continue
                if i+1 < len(flowerbed) and flowerbed[i+1] == 1:
                    i += 1
                    continue
                else:
                    flowerbed[i] = 1
                    flowersPlotted += 1
                    i += 1
        return flowersPlotted >= n
                
        