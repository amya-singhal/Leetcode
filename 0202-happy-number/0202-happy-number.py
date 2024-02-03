class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visited = set()
        while (True):
            if n in visited:
                return False
            tmp = 0
            for digit in str(n):
                square = int(digit)*int(digit)
                tmp += square
            if tmp == 1:
                return True
            visited.add(n)
            n = tmp
            