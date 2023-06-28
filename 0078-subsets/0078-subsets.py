class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def helper(tmp, nums):
            if tmp:
                if tmp not in ans:
                    ans.append(tmp)
            if not nums:
                return
            for i in range(0, len(nums)):
                helper(tmp + [nums[i]], nums[i+1:])
        helper([], nums)
        return ans