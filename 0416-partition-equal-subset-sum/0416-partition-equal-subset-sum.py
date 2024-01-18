class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2 != 0:
            return False
        target = sumNums / 2
        s = set()
        s.add(nums[0])
        for i in range(1, len(nums)):
            if target in s:
                return True
            tmp = set()
            for n in s:
                tmp.add(n)
                tmp.add(n+nums[i])
                tmp.add(nums[i])
            s = tmp
        return False