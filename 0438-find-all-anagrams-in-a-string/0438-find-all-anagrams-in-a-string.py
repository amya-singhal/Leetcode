class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        s="cbaebabacd" p = "abc"
        hvS = hash(cba), hvP = hash(abc)
        
        ans = [0, 6]
        """
        hvS, hvP = 0, 0
        if len(s) < len(p):
            return []
        ans = []
        for i in range(len(p)):
            hvS += hash(s[i])
            hvP += hash(p[i])
        if hvS == hvP:
            ans.append(0)
        for i in range(len(p), len(s)):
            hvS = hvS - hash(s[i-len(p)]) + hash(s[i])
            if hvS == hvP:
                ans.append(i-len(p)+1)
        return ans
        