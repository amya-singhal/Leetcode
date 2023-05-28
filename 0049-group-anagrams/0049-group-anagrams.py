class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            x = ''.join(sorted(s))
            if (x in d):
                d[x].append(s)
            else:
                d[x] = [s]
        return d.values()
        