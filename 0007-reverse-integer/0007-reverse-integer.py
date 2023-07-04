class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        negative = 1
        if x < 0:
            negative = -1
            x = -x
        while x:
            r = r * 10 + x % 10
            x //= 10
        if r > pow(2, 31):
            return 0
        return negative*r