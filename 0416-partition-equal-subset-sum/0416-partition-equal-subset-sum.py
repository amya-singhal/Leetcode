class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        s = set()
        s.add(0)
        for i in range(len(nums)-1, -1, -1):
            next = set()
            for x in s:
                next.add(nums[i] + x)
                next.add(x)
                s = next
            # print(s)
            if target in s:
                return True
        return False