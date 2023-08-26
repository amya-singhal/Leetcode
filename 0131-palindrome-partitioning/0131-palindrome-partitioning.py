class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def checkPalindrome(string):
            l = 0
            r = len(string) - 1
            while l<=r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        # visited = set()
        def helper(s, tmp):
            nonlocal ans
            if len(s) == 0:
                # print(tmp)
                ans.append(tmp.copy())
            for i in range(len(s)):
                if checkPalindrome(s[:i+1]):
                    # tmp.append(s[:i+1])
                    helper(s[i+1:], tmp+[s[:i+1]])
                    # tmp.remove(s[:i+1])
        helper(s, [])
        return ans
                
                    