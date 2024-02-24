class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        s = "ababcbacbdefegdehijhklij"
        lo = [a:6, b:8, c:7, ....]
        "qiejxqfnqceocmy"
        """
        lo = defaultdict(int)
        for i in range(len(s)):
            lo[s[i]] = i
        i = 0
        ans = []
        while i < len(s):
            start = lo[s[i]]
            tmp = s[i:start]
            j = 0
            while (j < start):
                if lo[s[j]] <= start:
                    j += 1
                    continue
                else:
                    start = lo[s[j]]
                    j += 1
            tmp = s[i:start+1]
            ans.append(len(tmp))
            i = start+1
        return ans
            
            
            