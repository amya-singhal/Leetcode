class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # s = ")()())"
        # s = ")())(())"
        # s = "()(()"
        # tmp = 2
        # stack = [-1,0,]
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans
        