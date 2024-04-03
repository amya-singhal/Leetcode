class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(index, tmp, visit):
            if index >= len(nums):
                if tmp not in ans:
                    ans.append(tmp)
            for i in range(len(nums)):
                if i not in visit:
                    visit.add(i)
                    helper(index+1, tmp+[nums[i]], visit)
                    visit.remove(i)
        helper(0, [], set())
        return ans