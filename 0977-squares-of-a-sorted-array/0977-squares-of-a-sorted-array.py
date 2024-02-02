class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l = 0
        r = len(nums)-1
        while l <= r:
            sl = nums[l]*nums[l]
            sr = nums[r]*nums[r]
            if sl > sr:
                ans.insert(0, sl)
                l += 1
            else:
                ans.insert(0, sr)
                r -= 1
        return ans