class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {}
        m[')'] = '('
        m['}'] = '{'
        m[']'] = '['
        for i in range(len(s)-1,-1,-1):
            if len(stack) > 0:
                if stack[-1] not in m: return False
                elif m[stack[-1]] == s[i]:
                    stack.pop()
                    continue
            stack.append(s[i])
        return len(stack) == 0