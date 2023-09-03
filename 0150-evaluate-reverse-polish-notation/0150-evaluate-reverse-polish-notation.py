class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = {
            '+': (lambda x,y: x+y),
            '-': (lambda x,y: x-y),
            '*': (lambda x,y: x*y),
            '/': (lambda x,y: x/y)
        }
        for t in tokens:
            if t in operators:
                y = int(s.pop())
                x = int(s.pop())
                s.append(operators[t](x, y))
            else:
                s.append(t)
            # print(s)
        return int(s[-1])
            