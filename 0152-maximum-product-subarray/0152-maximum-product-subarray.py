class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 2,3,-2,48
        # 2,3,2,4
        # -2,-3,-2,-4: -2,6,-12,48
        # 2 values, maxi, mini
        ans, maxi, mini = max(nums), nums[0], nums[0]
        for n in nums[1:]:
            if n == 0:
                maxi, mini = 1, 1
                continue
            tmp = maxi*n
            maxi = max(n, mini*n, tmp)
            mini = min(n, mini*n, tmp)
            ans = max(ans, maxi)
            # print(ans, maxi, mini)
        return ans