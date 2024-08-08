class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        keys = count.keys()
        
        for key in sorted(keys):
            if count[key] > 0:
                for i in range(1, groupSize):
                    # print(key, count[key])
                    if count[key+i] < count[key]:
                        return False
                    count[key+i] -= count[key]             
        return True