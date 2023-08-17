class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        # for i in hand:
        #     heapq.heappush(h, i)
        counterA = Counter(hand)
        h = list(counterA.keys())
        heapq.heapify(h)
        # print(h)
        # print(h)
        # print(counterA)
        # sortA = sorted(hand)
        while(h):
            x = h[0]
            for i in range(x, x+groupSize):
                if i not in counterA:
                    return False
                counterA[i] -= 1
                if counterA[i] == 0:
                    if i != h[0]:
                        return False
                    heapq.heappop(h)
            # print(h)
        return True