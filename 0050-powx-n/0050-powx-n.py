class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, absn):
            if x == 0:
                return 0
            if absn == 0:
                return 1
            res = helper(x, absn//2)
            res = res*res
            if absn % 2 == 1:
                res = res*x
            return res
        absn = abs(n)
        ans = helper(x, absn)
        if n < 0:
            return 1/ans
        return ans