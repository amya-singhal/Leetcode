class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        if ls1 > ls2:
            return False
        hvs1, hvs2 = 0, 0
        for i in s1:
            hvs1 += hash(i)
        for i in range(ls1):
            hvs2 += hash(s2[i])
        if hvs1 == hvs2:
            return True
        for i in range(ls1, ls2):
            hvs2 = hvs2 - hash(s2[i-ls1]) + hash(s2[i])
            if hvs1 == hvs2:
                return True
        return False