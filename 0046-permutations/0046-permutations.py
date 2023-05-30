class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = len(nums)
        def recur(tmp):
            if (len(tmp) == l):
                ans.append(tmp.copy())
                return
            for i in nums:
                if (i not in tmp):
                    tmp.append(i)
                    recur(tmp)
                    tmp.pop()
            
        recur([])
        return ans