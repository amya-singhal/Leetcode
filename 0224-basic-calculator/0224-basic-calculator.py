class Solution:
    def calculate(self, s: str) -> int:
        # "(1+(4+5+2)-3)+(6+8)", "-()"
        # stack = [0,+,1,+ 
        # answer = 0, 1, 0, 4+5 = 9+1*2 = 11+ 1 = 12
        # sign = 1, -1
        # curr = 0, 1, 0, 4, 0, 5, 0, 2, 0
        # '(', output and sign in stack
        # digit, num = digit
        # sign'+-', add sign*num into answer and change sign 
        # ')', add sign*num into answer, pop stack twice(1,2) and answer 1= 2
        stack, answer, sign, num = [], 0, 1, 0
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
                answer = 0
                sign = 1
            elif i == ')':
                answer += sign*num
                newsign = stack.pop()
                prevoutput = stack.pop()
                answer *= newsign
                answer += prevoutput
                num = 0
                sign = 1
        return answer + sign*num
                