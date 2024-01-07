class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        valid = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    valid = max(valid, i-stack[-1])
        return valid