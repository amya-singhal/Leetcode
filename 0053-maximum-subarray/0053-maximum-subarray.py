class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        answer, tmp = float('-inf'), 0
        for i in range(0, len(nums)):
            tmp += nums[i]
            answer = max(answer, tmp)
            if tmp < 0:
                tmp = 0
        return answer