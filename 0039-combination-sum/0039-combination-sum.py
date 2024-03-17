class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(tmp, n, index):
            nonlocal target
            if n == target:
                ans.append(tmp[:])
                return
            if n > target or index >= len(candidates):
                return
            tmp.append(candidates[index])
            helper(tmp, n+candidates[index], index)
            tmp.pop()
            helper(tmp, n, index+1)
        helper([], 0, 0)
        return ans
                    