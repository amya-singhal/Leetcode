class Solution:
    def checkValidString(self, s: str) -> bool:
        stacko = []
        stacks = []
        for i in range(len(s)):
            if s[i] == '(':
                stacko.append(i)
            elif s[i] == '*':
                stacks.append(i)
            else:
                if stacko:
                    stacko.pop()
                elif stacks:
                    stacks.pop()
                else:
                    return False
        while stacko:
            if not stacks:
                return False
            elif stacko[-1] < stacks[-1]:
                stacko.pop()
                stacks.pop()
            else:
                return False
        return True
                
    