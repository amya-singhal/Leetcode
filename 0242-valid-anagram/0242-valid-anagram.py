class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        print(d)
        for j in t:
            d[j] -= 1
            if d[j] == 0:
                d.pop(j)
        print(d)
        if len(d) != 0:
            return False
        return True