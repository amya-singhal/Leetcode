class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2
        s = set()
        s.add(0)
        for i in range(len(nums)):
            tmp = set()
            for x in s:
                tmp.add(x)
                tmp.add(x+nums[i])
            s = tmp
        if target in s:
            return True
        return False