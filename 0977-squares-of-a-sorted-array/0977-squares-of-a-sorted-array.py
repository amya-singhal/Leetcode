class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l = 0
        r = len(nums)-1
        while l <= r:
            sl = nums[l]*nums[l]
            sr = nums[r]*nums[r]
            if sl > sr:
                ans.append(sl)
                l += 1
            else:
                ans.append(sr)
                r -= 1
        ans.reverse()
        return ans