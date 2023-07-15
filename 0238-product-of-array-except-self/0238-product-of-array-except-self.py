class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        count = len(nums)
        for i in range(0, count):
            answer.append(1)
        y = nums[0]
        for i in range(1, count):
            answer[i] = y * answer[i]
            y = y * nums[i]
        x = 1
        for i in reversed(range(0, count)):
            answer[i] = x * answer[i]
            x = x * nums[i]
        return answer