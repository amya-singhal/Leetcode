import sortedcontainers
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        # x = 2, 3, 7
        # [2,10], [3, 15], [7, ]
        tmp = []
        for x, y, h in buildings:
            tmp.append((x, -h))
            tmp.append((y, h))
            
        tmp.sort()
        # print(tmp)
        skyline = []
        maxH = 0
        height = sortedcontainers.SortedList([0])
        for t1, t2 in tmp:
            # print(height)
            # start
            if t2 < 0:
                height.add(-t2)
            # end
            else:
                height.remove(t2)
            tmpMaxH = max(height)
            # print(tmpMaxH)
            if tmpMaxH != maxH:
                maxH = tmpMaxH
                skyline.append([t1, maxH])
        return skyline
            