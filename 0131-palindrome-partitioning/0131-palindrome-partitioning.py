class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, ans, tmp):
            if not s:
                ans.append(tmp)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], ans, tmp+[s[:i]])
        ans = []
        dfs(s, ans, [])
        return ans