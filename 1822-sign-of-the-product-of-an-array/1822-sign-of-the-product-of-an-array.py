class Solution(object):
    def arraySign(self, nums):
        negative = 1
        for n in nums:
            if n == 0:
                return 0
            elif n > 0:
                negative = negative
            else:
                if negative == 1:
                    negative = -1
                else:
                    negative = 1
        return negative
                
        """
        :type nums: List[int]
        :rtype: int
        """
        