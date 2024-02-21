class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s = "ADOBECODEBANC", t = "ABC"
        need = {a:1, b:1, c:1}
        have = {a:0, d:1, o:1, b:1, e:1, c:1}
        needc = 3
        havec = 2
        """
        need = defaultdict(int)
        have = defaultdict(int)
        lT = len(t)
        lS = len(s)
        if lT > lS:
            return ""
        ans = ""
        ansl = 0
        ansr = lS
        for i in range(lT):
            need[t[i]] += 1
        needCount = len(need)
        haveCount = 0
        j = 0
        for i in range(lS):
            have[s[i]] += 1
            if s[i] in need and have[s[i]] == need[s[i]]:
                haveCount += 1
            while (needCount == haveCount):
                if (i-j) < (ansr-ansl):
                    ans = s[j:i+1]
                    ansl, ansr = j, i
                have[s[j]] -= 1
                if s[j] in need and have[s[j]] < need[s[j]]:
                    haveCount -= 1
                j += 1
        return ans
            
                
        
        
            
            
            
        