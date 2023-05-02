class Solution(object):
    def searchInsert(self, nums, target):
        index = 0
        x = nums[index]
        while (target != x):
            if (target > x):
                if (index == (len(nums) - 1)):
                    return index+1
                index += 1
                x = nums[index]
            else:
                return index
        return index
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        