class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def helper(tmp, x):
            if x == len(nums):
                return
            tmp.append(nums[x])
            ans.append(tmp.copy())
            helper(tmp, x+1)
            tmp.pop()
            helper(tmp, x+1)
        helper([], 0)
        return ans