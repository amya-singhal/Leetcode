class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["4","13","5","/","+"]
        s = []
        """
        stack = []
        operators = '+-*/'
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()
                ans = 0
                if i == '+':
                    ans = first + second
                elif i == '-':
                    ans = first - second
                elif i == '*':
                    ans = first * second
                else:
                    ans = first / second
                stack.append(int(ans))
        return stack.pop()