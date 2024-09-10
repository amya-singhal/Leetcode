class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        s = set()
        s.add(nums[0])
        for i in range(1, len(nums)):
            new_s = set()
            for x in s:
                new_s.add(x)
                new_s.add(x+nums[i])
            s = new_s
        return target in s