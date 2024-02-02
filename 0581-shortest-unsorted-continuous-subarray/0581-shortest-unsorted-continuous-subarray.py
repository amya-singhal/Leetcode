class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        first, last = -1,-1
        big, small = nums[0], nums[-1]
        for i in range(1, len(nums)):
            if nums[i] >= big:
                big = nums[i]
            else:
                last = i
        for j in range(len(nums)-2, -1, -1):
            if nums[j] <= small:
                small = nums[j]
            else:
                first = j
        if first == last:
            return 0
        return last-first+1
        