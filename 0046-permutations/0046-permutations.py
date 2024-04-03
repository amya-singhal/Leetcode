class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # []
        n = len(nums)
        def helper(index, tmp):
            if index >= n:
                ans.append(tmp)
                return
            for i in nums:
                if i not in tmp:
                    helper(index+1, tmp+[i])
        helper(0, [])
        return ans
            