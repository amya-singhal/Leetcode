class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        s = []
        o = "+-/*"
        for i in range(len(tokens)):
            # print(s)
            if tokens[i] in o:
                second = s.pop()
                first = s.pop()
                a = 0
                oper = tokens[i]
                if oper == '+':
                    a = first + second
                if oper == '-':
                    a = first - second
                if oper == '/':
                    a = first / second
                if oper == '*':
                    a = first * second
                s.append(int(a))
            else:
                s.append(int(tokens[i]))
        return s.pop()