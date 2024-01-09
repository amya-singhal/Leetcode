class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        lastIndex = len(nums)-1
        curr = 0
        jumps = 0
        while(curr < len(nums)):
            maxReached = nums[curr]+curr
            if maxReached >= len(nums)-1:
                return jumps+1
            for i in range(curr+1, maxReached+1):
                if (nums[i]+i > nums[curr]+curr):
                    curr = i
            jumps += 1
        return jumps