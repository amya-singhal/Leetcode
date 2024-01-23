class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = defaultdict(int)
        # {a:1,b:1,c:1}
        for i in t:
            need[i] += 1
        have = defaultdict(int)
        # {a:1, d:2, o:2, b:2, e:2, c:1}
        needCount = len(need)
        haveCount = 0
        # 3
        l = 0
        # 1
        L, R = 0 , len(s)
        length = float('inf')
        # 6, 
        for r in range(len(s)):
            have[s[r]] += 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                haveCount += 1
            while haveCount == needCount:
                if R-L+1 > r-l+1:
                    L, R = l, r
                    length = r-l+1
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    haveCount -= 1
                l += 1
        if length != float('inf'):
            return s[L:R+1]
        return ""