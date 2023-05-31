class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # using sliding window and hash values
        pL = len(p)
        sL = len(s)
        S, P = 0, 0
        if (sL < pL):
            return []
        ans = []
        for i in range(pL):
            S += hash(s[i])
            P += hash(p[i])
        if (S == P):
            ans.append(0)
        for i in range(pL, sL):
            S += hash(s[i]) - hash(s[i - pL])
            if (S == P):
                ans.append(i - pL + 1)
        return ans