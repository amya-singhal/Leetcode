class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        num = 0
        answer = 0
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i in '+-':
                answer += sign*num
                num = 0
                if i == '+':
                    sign = 1
                else:
                    sign = -1
            elif i == '(':
                stack.append(answer)
                stack.append(sign)
                sign = 1
                answer = 0
            elif i == ')':
                answer += sign*num
                answer *= stack.pop()
                answer += stack.pop()
                num = 0
        return answer + sign*num