class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(tmp, t):
            if t > target:
                return
            if t == target:
                tmp = sorted(tmp)
                if tmp not in ans:
                    ans.append(tmp[:])
                return
            else:
                for i in candidates:
                    helper(tmp+[i], t+i)
        helper([], 0)
        return ans
        