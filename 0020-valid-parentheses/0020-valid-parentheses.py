class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i== '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if not((prev == '(' and i == ')') or (prev == '[' and i == ']') or (prev == '{' and i == '}')):
                    return False
        if not stack:
            return True
        return False
                    
                    