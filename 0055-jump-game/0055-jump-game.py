class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(0, len(nums)-1)):
            if i+nums[i] >= goal:
                goal = i
        if (goal == 0):
            return True
        else:
            return False