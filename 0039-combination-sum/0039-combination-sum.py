class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        visit = []
        def helper(tmp, n):
            nonlocal target
            if n == target:
                tmp = sorted(tmp)
                if tmp not in visit:
                    ans.append(tmp)
                    visit.append(tmp)
            if n > target:
                return
            for i in candidates:
                if i+n <= target:
                    helper(tmp+[i], i+n)
        helper([], 0)
        return ans
                    