class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        x = 0
        finalCount = 0
        count = 0
        while(x < len(s)):
            if (s[x] in visited):
                x = visited[s[x]]+1
                if (count > finalCount):
                    finalCount = count
                count = 0
                visited = {}
            else:
                visited[s[x]] = x
                count += 1
                x += 1
        finalCount = max(finalCount, count)
        return finalCount
        """
        s3-> pewpabc
        a3-> 0120123
        ans = 0
        for i in range(0, len(s)):
            tmp = ""
            for j in range(i, len(s)):
                if (s[j] in tmp):
                    break
                tmp += s[j]
            if (len(tmp) > ans):
                ans = len(tmp)
        return ans
        """
        
        
                
            