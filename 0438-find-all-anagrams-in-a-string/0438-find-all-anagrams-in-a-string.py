class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # using sliding window and hash values
        """
        ans = []
        s -> cbaebabacd
        p -> abc
        lP = 10
        lS = 3
        S = hash(a) + hash(b) + hash(c)
        P = hash(c) + hash(b) + hash(a) = hash(abc)
        base condition:
        S == P -> 
        ans = [0]
        for loop:
        S = hash(b) + hash(a) + hash(e)
        S != P
        S = hash(a) + hash(e) + hash(b)
        S != P
        S = hash(e) + hash(b) + hash(a)
        S != P
        S = hash(b) + hash(a) + hash(b)
        S != P
        S = hash(a) + hash(b) + hash(a)
        S != P
        S = hash(a) + hash(b) + hash(c)
        S == P
        ans = [6]
        """
        ans = []
        lP = len(p)
        lS = len(s)
        S,P = 0,0
        if (lS < lP):
            return []
        for i in range(lP):
            S += hash(s[i])
            P += hash(p[i])
        if S==P:
            ans.append(0)
        for i in range(lP, lS):
            S += hash(s[i]) - hash(s[i-lP])
            if (S == P):
                ans.append(i-lP + 1)
        return ans