class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            one, two = 0, 0
            for n in nums:
                newR = max(one+n, two)
                one  = two
                two = newR
            return two
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))