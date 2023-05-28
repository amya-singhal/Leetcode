class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(tmp, candidates, sum):
            if (sum == target):
                tmp.sort()
                if (tmp not in ans):
                    ans.append(tmp)
                return
            elif (sum < target):
                for i in candidates:
                    helper(tmp + [i], candidates, sum+i)
            else:
                return                
        helper([], candidates, 0)
        return ans