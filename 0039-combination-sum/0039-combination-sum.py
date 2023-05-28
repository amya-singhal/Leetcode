class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(tmp, x, sum):
            if sum == target:
                ans.append(tmp[:])
                return
            if (sum > target or x >= len(candidates)):
                return
            tmp.append(candidates[x])
            helper(tmp, x, sum+candidates[x])
            tmp.pop()
            helper(tmp, x+1, sum)
            return ans
        return helper([], 0, 0)
        

        