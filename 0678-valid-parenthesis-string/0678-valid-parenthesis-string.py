class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  # Minimum number of unmatched '('
        high = 0  # Maximum number of unmatched '('

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                if low > 0:
                    low -= 1
                high -= 1
            else:  # char == '*'
                if low > 0:
                    low -= 1
                high += 1

            # If at any point, the number of unmatched '(' is negative, it's invalid
            if high < 0:
                return False

        # Valid if and only if all '(' can be matched
        return low == 0