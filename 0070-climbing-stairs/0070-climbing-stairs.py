class Solution(object):
    def climbStairs(self, n):
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        a = []
        a.append(0)
        a.append(1)
        a.append(2)
        for i in range(3, n+1):
            result = a[i-1]+a[i-2]
            a.append(result)
        return a[n] 
        """
        :type n: int
        :rtype: int
        """
        