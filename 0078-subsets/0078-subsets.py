class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])
        if (len(nums) == 1):
            ans.append([nums[0]])
            return ans
        def recur(tmp, x):
            if (x == len(nums)):
                return
            tmp.append(nums[x])
            ans.append(tmp.copy())
            recur(tmp, x+1)
            tmp.pop()
            recur(tmp, x+1)
        recur([], 0)
        return ans