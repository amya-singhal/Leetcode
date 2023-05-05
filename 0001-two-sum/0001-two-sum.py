class Solution(object):
    def twoSum(self, nums, target):
        x = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in x:
                return [x[diff], i]
            x[v] = i
        return
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        