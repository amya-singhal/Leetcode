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
        l = 0
        maxi = 0
        ans = []
        for r in range(len(s)):
            maxi = max(maxi, lo[s[r]])
            if r == maxi:
                ans.append(r-l+1)
                l = r+1
        return ans
            
            
            