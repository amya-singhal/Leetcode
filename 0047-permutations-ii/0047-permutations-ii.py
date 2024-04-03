class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(tmp, visit):
            if len(tmp) == len(nums):
                if tmp not in ans:
                    ans.append(tmp)
            for i in range(len(nums)):
                if i not in visit:
                    visit.add(i)
                    helper(tmp+[nums[i]], visit)
                    visit.remove(i)
        helper([], set())
        return ans