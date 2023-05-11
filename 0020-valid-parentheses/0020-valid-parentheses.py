class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            else:
                if (stack == []):
                    return False
                x = stack.pop()
                if ((x == '(' and s[i] != ')') or (x == '[' and s[i] != ']') or 
                   (x == '{' and s[i] != '}')):
                    return False
                else:
                    continue
        if (stack == []):
            return True
        else:
            return False
        