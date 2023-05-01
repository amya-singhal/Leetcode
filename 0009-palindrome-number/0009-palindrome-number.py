class Solution(object):
    def isPalindrome(self, x):
        stringx = str(x)
        l = 0
        h = len(stringx) - 1
        while l <= h:
            if (stringx[l] != stringx[h]):
                return False
            l += 1
            h -= 1
        return True
        """
        :type x: int
        :rtype: bool
        """
        