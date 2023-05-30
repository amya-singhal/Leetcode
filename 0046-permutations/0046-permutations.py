class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = len(nums)
        def recur(tmp, nums):
            if (len(nums) == 0):
                if (len(tmp) == l):
                    ans.append(tmp)
                return
            for i in range(0, len(nums)):
                recur(tmp + [nums[i]], nums[:i] + nums[i+1:])
            
        recur([], nums)
        return ans