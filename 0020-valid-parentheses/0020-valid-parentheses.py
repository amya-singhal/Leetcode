class Solution:
    def isValid(self, s: str) -> bool:
        """
        i : {()()  
        x = ['[', '{', '(']
        stack = {
        stack = {
        ()
        stack = {
        ()
        stack is not empty
        not valid
        """
        stack = []
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                stack.append(i)
            else:
                if (len(stack) == 0):
                    return False # there is no open bracket preceding the closed one
                x = stack.pop()
                if (x == '(' and i != ')' or x == '[' and i != ']' or x == '{' and i != '}'):
                    return False
        if (len(stack) != 0):
            return False
        return True
        