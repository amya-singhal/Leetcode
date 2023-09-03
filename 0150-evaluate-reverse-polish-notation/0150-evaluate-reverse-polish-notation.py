class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = ['+','-','*','/']
        for t in tokens:
            if t in operators:
                y = int(s.pop())
                x = int(s.pop())
                if t == '+':
                    z = x + y
                elif t == '-':
                    z = x - y
                elif t == '*':
                    z = x * y
                else:
                    z = x / y
                s.append(z)
            else:
                s.append(t)
            # print(s)
        return int(s.pop())
            