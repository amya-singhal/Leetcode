class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(tmp, sum):
            if (sum == target):
                tmp.sort()
                if (tmp not in ans):
                    ans.append(tmp)
                return
            elif (sum > target):
                return
            for i in candidates:
                helper(tmp + [i], sum+i)              
        helper([], 0)
        return ans