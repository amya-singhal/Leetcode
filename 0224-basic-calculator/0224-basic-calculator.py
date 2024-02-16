class Solution:
    def calculate(self, s: str) -> int:
        # if digits: add to stack
        # if open brack: add to stack
        # if close brack: 
        # if operator: sign
        # (1+(4+5+2)-3)+(6+8)
        ans = 0
        num = 0
        z = []
        sign = 1
        for i in s:
            if i.isdigit():
                num = num*10+int(i)
            elif i =='(':
                z.append(ans)
                z.append(sign)
                ans = 0
                sign = 1
            elif i == ')':
                ans += num*sign
                newsign = z.pop()
                output = z.pop()
                ans = ans*newsign
                ans = ans + output
                num = 0
                sign = 1   
            elif i in '+-':
                ans += sign*num
                num = 0
                if i == '+':
                    sign = 1
                if i == '-':
                    sign = -1
        return ans + sign*num
                    
                
        