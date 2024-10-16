class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = ceil(sum(piles)/h), max(piles)
        while l < r:
            mid = l+(r-l)//2
            tmp = 0
            for pile in piles:
                tmp += ceil(pile/mid)
                if h < tmp:
                    break
            if tmp <= h:
                r = mid
            else:
                l = mid+1
        
        return r
        