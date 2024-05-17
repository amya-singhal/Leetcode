class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        needCount = len(need)
        haveCount = 0
        ansL = float(inf)
        ans = ""
        l,r = 0,0
        while (r < len(s)):
            while needCount == haveCount:
                if ansL > r-l+1:
                    ansL = r-l+1
                    ans = s[l:r]
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    haveCount -= 1
                l += 1
            else:
                have[s[r]] += 1
                if s[r] in need and have[s[r]] == need[s[r]]:
                    haveCount += 1
                r += 1
        while needCount == haveCount:
                if ansL > r-l+1:
                    ansL = r-l+1
                    ans = s[l:r]
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    haveCount -= 1
                l += 1
        return ans