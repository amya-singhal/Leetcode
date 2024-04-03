class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(tmp, count):
            if len(tmp) == len(nums):
                if tmp not in ans:
                    ans.append(tmp)
                return
            for i in count:
                if count[i] > 0:
                    count[i] -= 1
                    helper(tmp+[i], count)
                    count[i] += 1
        count = Counter(nums)
        helper([], count)
        return ans